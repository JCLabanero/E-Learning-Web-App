# Generated by Django 4.2.7 on 2023-12-03 02:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_account_type_alter_learn1_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learn1',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 10, 10, 42, 295488), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 10, 10, 42, 296489), verbose_name='date published'),
        ),
    ]
