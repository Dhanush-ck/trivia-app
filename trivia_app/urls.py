"""
URL configuration for trivia_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name="welcome"),
    path('signup', views.signup, name="signup"),
    path('start ', views.start_trivia, name='start'),
    path('trivia', views.trivia_page, name='trivia'),
    path('check', views.check_answer, name='check'),
    path('restart', views.restart_trivia, name='restart'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('levels', views.leaderboard_level, name='levels'),
    path('level', views.level, name='level'),
    path('signin', views.signin, name='signin'),
    path('result', views.result, name='result'),
    path('reset', views.reset_password, name='reset'),
    path('change', views.change_password, name='change'),
    path('logout', views.logout, name="logout"),
    path('ai', views.ai_view, name="ai"),
    path('ai/trivia', views.ai_trivia, name="ai/trivia"),
    path('ai/result', views.ai_result, name="ai/result"),
]
