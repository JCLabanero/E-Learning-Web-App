# Generated by Django 4.2.7 on 2023-12-03 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_learn1_published_alter_lesson_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='main/assets/thumbnails/user-default.png', upload_to='main/static/main/assets/thumbnails'),
        ),
        migrations.AlterField(
            model_name='learn1',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 14, 15, 46, 848677), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 14, 15, 46, 849677), verbose_name='date published'),
        ),
    ]