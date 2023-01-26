from django.db import models


class Persons(models.Model):
    name = models.CharField('Имя', max_length=200, blank=True)
    address = models.CharField('Адрес', max_length=200, blank=True)
    work = models.CharField('Работа', max_length=200, blank=True)
    age = models.DateField('Возраст',  max_length=200, blank=True)