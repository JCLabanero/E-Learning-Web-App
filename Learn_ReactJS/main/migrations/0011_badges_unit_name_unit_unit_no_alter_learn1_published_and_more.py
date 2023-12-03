# Generated by Django 4.2.7 on 2023-12-02 23:54

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_merge_20231203_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='{% static "main/assets/badges" %}')),
                ('name', models.CharField(max_length=255)),
                ('requirements', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='unit',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='unit_no',
            field=models.IntegerField(default=1, verbose_name='Unit No.'),
        ),
        migrations.AlterField(
            model_name='learn1',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 7, 53, 31, 161231), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 7, 53, 31, 162232), verbose_name='date published'),
        ),
    ]