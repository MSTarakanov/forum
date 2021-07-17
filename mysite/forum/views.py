from django.shortcuts import render
from .models import Messages
from django.contrib.auth.forms import UserCreationForm

def index(request):
    messages = Messages.objects.all()
    return render(request, 'forum/index.html', {'messages': messages})


def register(request):
    form = UserCreationForm()
    return render(request, 'forum/register.html', {'form': form})


def login(request):
    return render(request, 'forum/login.html')
