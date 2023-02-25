from django.db import models
from ckeditor import fields
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	firstname = models.CharField('Имя*', max_length=512)
	lastname = models.CharField('Фамилия*', max_length=512)
	def __str__(self):
		return self.username
	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'


class Event(models.Model):
	name = models.CharField('Название', max_length=512)
	desc = fields.RichTextField('Описание', blank=True, null=True)
	img = models.CharField('Картинка', max_length=5096, blank=True, null=True)
	start = models.DateTimeField('Начало')
	finish = models.DateTimeField('Конец')
	def __str__(self) -> str:
		return self.name
	class Meta:
		verbose_name = 'Событие'
		verbose_name_plural = 'События'


class Invited(models.Model):
	event = models.ForeignKey('Event', on_delete=models.CASCADE)
	user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
	def __str__(self):
		return str(self.event)
	class Meta:
		verbose_name = 'Приглашение'
		verbose_name_plural = 'Приглашения'