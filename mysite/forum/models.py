from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    sex = models.ForeignKey('Sex', on_delete=models.PROTECT, null=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/%Y/%m/%d/', null=True)
    bio = models.CharField(verbose_name='Био', max_length=100, blank=True)

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
    user = models.ForeignKey(Users, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']