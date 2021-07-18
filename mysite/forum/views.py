from django.shortcuts import render, redirect
from .models import Messages
from .forms import UserLoginForm, MessageAddForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
# from .forms import SignUpForm

def index(request):
    if request.method == 'POST':
        form = MessageAddForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            text = form.cleaned_data['text']
            user = request.user
            Messages.objects.create(text=text, user=user)
            return redirect('home')
    else:
        form = MessageAddForm()
    forum_messages = Messages.objects.all()
    return render(request, 'forum/index.html', {'forum_messages': forum_messages, 'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрированы!')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserCreationForm()
    return render(request, 'forum/register.html', {'form': form, 'subtitle': 'Регистрация'})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'forum/login.html', {'form': form, 'subtitle': 'Авторизация'})


def user_logout(request):
    logout(request)
    return redirect('home')
