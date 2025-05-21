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
    path('signup/', views.home, name="signup"),
    path('start/ ', views.start_trivia, name='start'),
    path('trivia/', views.trivia_page, name='trivia'),
    path('check/', views.check_answer, name='check'),
    path('restart/', views.restart_trivia, name='restart'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user, name='login'),
]
