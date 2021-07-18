from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# class Users(AbstractUser):
#     sex = models.ForeignKey('Sex', on_delete=models.PROTECT, null=True)
#     photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m/%d/', null=True)
#     bio = models.CharField(verbose_name='Био', max_length=100, blank=True)
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'


class SiteAccountManager(BaseUserManager):
    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser is_staff must be True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser is_superuser must be True.')

        return self.create_user(username, email, password, **other_fields)

    def create_user(self, username, email, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class SiteUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=20, unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=150, blank=True)
    second_name = models.CharField(verbose_name='Фамилия', max_length=150, blank=True)
    fathers_name = models.CharField(verbose_name='Отчество', max_length=150, blank=True)
    start_date = models.DateTimeField(verbose_name='Дата регистрации', default=timezone.now)
    is_staff = models.BooleanField(verbose_name='Модератор', default=False)
    is_active = models.BooleanField(verbose_name='Активный пользователь', default=False)
    sex = models.ForeignKey('Sex', on_delete=models.PROTECT, null=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m/%d/', null=True)
    birth_date = models.DateTimeField(verbose_name='Дата рождения', null=True)
    about = models.TextField(verbose_name='Био', max_length=500, blank=True)

    objects = SiteAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Sex(models.Model):
    definition = models.CharField(max_length=5, verbose_name='Обозначение', db_index=True)

    def __str__(self):
        return self.definition

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'
        ordering = ['definition']


class Messages(models.Model):
    text = models.TextField(verbose_name='Текст', max_length=150)
    created_at = models.DateTimeField(verbose_name='Дата отправки', auto_now_add=True)
    user = models.ForeignKey(SiteUser, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']



