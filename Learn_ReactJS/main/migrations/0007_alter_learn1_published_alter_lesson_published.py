# Generated by Django 4.2.7 on 2023-12-13 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_learn1_published_alter_lesson_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learn1',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 13, 13, 53, 3, 240765), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 13, 13, 53, 3, 241764), verbose_name='date published'),
        ),
    ]
