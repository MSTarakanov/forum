from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import SiteUser, Sex


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин* ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail* ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль* ', help_text='Пароль должен содержать не меньше 8 символов, состоять не только из цифр.', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль* ', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    second_name = forms.CharField(label='Фамилия', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fathers_name = forms.CharField(label='Отчество', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(label='Дата рождения', required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                      'type': 'date',
                                                                                      'id': 'date',
                                                                                      'name': 'date',
                                                                                      }))
    sex = forms.ModelChoiceField(empty_label='Выберите пол', label='Пол', required=False, queryset=Sex.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = SiteUser
        fields = ('username', 'email', 'password1', 'password2','second_name', 'first_name', 'fathers_name', 'birth_date',
                  'sex')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class MessageAddForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
    }))
