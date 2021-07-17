from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class MessageAddForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
    }))
