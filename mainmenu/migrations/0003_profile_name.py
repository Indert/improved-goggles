# Generated by Django 4.1.5 on 2023-01-23 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainmenu', '0002_profile_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, default='Ваш Аккаунт', max_length=200, null=True, verbose_name='Ваше Имя и Фамилия'),
        ),
    ]
