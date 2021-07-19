from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.timesince import timesince


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
    is_active = models.BooleanField(verbose_name='Активный пользователь', default=True)
    sex = models.ForeignKey('Sex', on_delete=models.PROTECT, blank=True, null=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    birth_date = models.DateTimeField(verbose_name='Дата рождения', blank=True, null=True)
    about = models.TextField(verbose_name='Био', max_length=500, blank=True)

    objects = SiteAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_age(self):
        if self.birth_date:
            age = ' '.join(timesince(self.birth_date).split()[0:2])
            if age[-1] == ',':
                age = age[:-1]
            return age
        return False

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
    text = models.TextField(verbose_name='Текст', max_length=500)
    created_at = models.DateTimeField(verbose_name='Дата отправки', auto_now_add=True)
    user = models.ForeignKey(SiteUser, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.pk)

    def get_created_date(self):
        return self.created_at
        # today = timezone.now().date()
        # if today == self.created_at.date():
        #     return 'Сегодня ' + self.created_at.strftime('%H:%M')
        # yesterday_delta = (timezone.now() - self.created_at).total_seconds()
        # if 86400 < yesterday_delta < 86400*2:
        #     return 'Вчера ' + self.created_at.strftime('%H:%M')
        # return today

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']
