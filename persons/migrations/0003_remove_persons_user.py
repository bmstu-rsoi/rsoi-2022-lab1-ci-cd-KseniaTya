# Generated by Django 4.1 on 2022-11-26 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_alter_persons_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persons',
            name='user',
        ),
    ]