# Generated by Django 4.1.5 on 2023-02-20 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainmenu', '0013_video_father'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='videos',
        ),
    ]
