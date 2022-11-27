from django.db import models


class Persons(models.Model):
    last_name = models.CharField('Фамилия', max_length=200, blank=True)
    first_name = models.CharField('Имя', max_length=200, blank=True)
    father_name = models.CharField('Отчество', max_length=200, blank=True)
    birthday = models.DateField('День рождения', blank=True)