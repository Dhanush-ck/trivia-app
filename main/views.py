from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from . models import Question
import random
from . forms import NameForm
from . forms import UserForm
# Create your views here.

def welcome(request):
    if request.method == 'POST':
        return redirect('signup')
    return render(request, 'welcome.html')

def home(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            password = form.cleaned_data['password']
            if not User.objects.filter(username=username).exists():
                    User.objects.create_user(username=username, password=password)
                    return redirect('dashboard')
        else:
            return render(request, 'home.html', {
            'form': form
        })
    form = NameForm()
    return render(request, 'home.html', {
        'form': form
    })

def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return redirect('dashboard')
        else:
            return render(request, 'user.html', {
        'form': form
    })

    form = UserForm()
    return render(request, 'user.html', {
        'form': form
    })
        
def dashboard(request):
    if request.method == 'POST':
        level = request.POST.get('level')
        request.session['level'] = level
        return redirect('start')
    return render(request, 'dashboard.html')

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
        name = request.session.get('username')
        score = request.session['score']
        return render(request, 'result.html', {
            'score': score,
            'name': name,
        })

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
    
def restart_trivia(request):
    request.session.flush()
    return redirect('dashboard')