# Generated by Django 4.2.7 on 2023-12-03 00:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_account_alter_assessment_lesson_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(default='{% static "main/assets/thumbnails/user-default.png" %}', upload_to='{% static "main/assets/thumbnails" %}'),
        ),
        migrations.AlterField(
            model_name='learn1',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 8, 28, 2, 578876), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 8, 28, 2, 578876), verbose_name='date published'),
        ),
    ]