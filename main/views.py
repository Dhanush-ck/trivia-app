from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .gemini import generate_response
from django.contrib.auth.models import User

from . models import Question
import random
from . forms import NameForm
from . forms import UserForm
from . forms import ResetForm
from . forms import ChangePasswordForm

import json

# Create your views here.

def welcome(request):
    if request.method == 'POST':
        return redirect('signup')
    return render(request, 'welcome.html')

def signup(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            if not User.objects.filter(username=username).exists():
                    User.objects.create_user(username=username, password=password)

                    question = form.cleaned_data['question']
                    answer = form.cleaned_data['answer']
                    user = User.objects.get(username=username)
                    user.profile.question = question
                    user.profile.answer = answer
                    user.profile.save()
                    request.session['username'] = username
                    return redirect('dashboard')
        else:
            return render(request, 'signup.html', {
            'form': form
        })
    form = NameForm()
    return render(request, 'signup.html', {
        'form': form
    })

def signin(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            request.session['username'] = username
            return redirect('dashboard')
        else:
            return render(request, 'signin.html', {
        'form': form
    })

    form = UserForm()
    return render(request, 'signin.html', {
        'form': form
    })

def reset_password(request):
    if request.method == 'POST':
        form = ResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            request.session['username'] = username
            return redirect('change')
        else:
            return render(request, 'reset.html', {
                'form': form,
            })
            
    form = ResetForm()
    return render(request, 'reset.html', {
        'form': form,
    })

def change_password(request):
    username = request.session['username']
    user = User.objects.get(username=username)
    question = user.profile.question
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            if answer == user.profile.answer:
                new_password = form.cleaned_data['password']
                if user.check_password(new_password):
                    form.add_error('password', 'Same Password')
                    return render(request, 'change.html', {
                        'form': form,
                        'question': question,
                    })
                user.set_password(new_password)
                user.save()
                return redirect('signin')
            else:
                form.add_error('answer', 'Answer Incorrect')
                return render(request, 'change.html', {
                    'form': form,
                    'question': question,
                })
    form = ChangePasswordForm()
    return render(request, 'change.html', {
        'form': form,
        'question': question,
    })

def dashboard(request):
    username = request.session['username']
    return render(request, 'dashboard.html', {
        'username':username,
    })

def leaderboard_level(request):
    if request.method == 'POST':
        level = request.POST.get('level')
        request.session['leaderboard_level'] = level
        return redirect('leaderboard')
    return render(request, 'leaderboard_level.html')

def leaderboard(request):
    level = request.session['leaderboard_level']
    current_level = level + '_score'
    users = []
    for user in User.objects.all().exclude(username="admin"):
        users.append({
            "name" : user.username,
            "score": getattr(user.profile, current_level),
        })
    users = sorted(users, key=lambda x:x['score'], reverse=True)
    return render(request, 'leaderboard.html', {
        'users' : users,
    })
        
def level(request):
    if request.method == 'POST':
        level = request.POST.get('level')
        request.session['level'] = level
        return redirect('start')
    return render(request, 'level.html')

def start_trivia(request):
    request.session['used_questions'] = []
    request.session['score'] = 0
    request.session['count'] = 0
    return redirect('trivia')

def trivia_page(request):

    used_ids = request.session['used_questions']
    level = request.session['level']
    remaining_questions = Question.objects.filter(difficulty=level).exclude(id__in=used_ids)
    count = request.session['count']

    if remaining_questions.exists() and count < 10:
        question = random.choice(list(remaining_questions))
        request.session['current_question_id'] = question.id
        used_ids.append(question.id)
        request.session['used_questions'] = used_ids
        return render(request, 'trivia.html', {'question': question})
    else :
        return redirect('result')

def check_answer(request):
    if request.method == 'POST':
        selected_option = int(request.POST.get('option-btn'))
        current_question_id = request.session.get('current_question_id')

        question = Question.objects.get(id=current_question_id)

        correct = (selected_option == question.correct_option)

        if correct :
            request.session['score'] = request.session.get('score', 0) + 1
        
        request.session['count'] = request.session.get('count', 0) + 1

        return redirect('trivia')
    
def result(request):
    name = request.session['username']
    score = request.session['score']
    user = User.objects.get(username=name)
    level = request.session['level']
    current_score = level + '_score'
    user_score = getattr(user.profile, current_score)
    if score > user_score:
        setattr(user.profile, current_score, score)
        user.profile.save()
    return render(request, 'result.html', {
        'score': score,
        'level': level,
        })
    
def restart_trivia(request):
    # request.session.flush()
    return redirect('dashboard')

def logout(request):
    request.session.flush()
    return redirect('welcome')

def chat_view(request):
    answer = None
    if request.method == 'POST':
        temp_prompt = request.POST.get('prompt')
        prompt = f"Generate {temp_prompt} 10 question json with question, 4 option and correct option can be assigned to variable"
        answer = generate_response(prompt)
        # print(answer)
    return render(request, 'chat.html', {'answer': answer})