from django.shortcuts import render, redirect
from . models import Question
import random

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        request.session['username'] = username
        return redirect('start')
    return render(request, 'home.html')

def start_trivia(request):
    request.session['used_ids'] = []
    return redirect('trivia')

def trivia_page(request):
    # name = request.session.get('username')
    used_ids = request.session.get('used_ids', [])

    available_ids = Question.objects.exclude(id__in=used_ids)
    
    question = random.choice(list(available_ids))

    used_ids.append(question.id)
    request.session['used_ids'] = used_ids
    
    return render(request, 'trivia.html', {
        'question': question,
    })