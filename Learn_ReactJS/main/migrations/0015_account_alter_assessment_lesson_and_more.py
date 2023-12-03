# Generated by Django 4.2.7 on 2023-12-03 00:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_learn1_published_alter_lesson_published_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=200, verbose_name='Username')),
                ('firstname', models.CharField(default='firstname', max_length=200, verbose_name='First Name')),
                ('lastname', models.CharField(default='lastname', max_length=200, verbose_name='Last Name')),
                ('email', models.CharField(default='email', max_length=200, verbose_name='Email')),
                ('password', models.CharField(default='password', max_length=200, verbose_name='Password')),
            ],
        ),
        migrations.AlterField(
            model_name='assessment',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.learn1'),
        ),
        migrations.AlterField(
            model_name='learn1',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 8, 21, 17, 479088), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 8, 21, 17, 479088), verbose_name='date published'),
        ),
    ]