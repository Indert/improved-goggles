# Generated by Django 4.1.5 on 2023-02-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainmenu', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='movies'),
        ),
    ]
