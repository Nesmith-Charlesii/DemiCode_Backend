# Generated by Django 3.1.7 on 2021-06-29 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_creator', '0011_auto_20210628_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creative',
            name='confirmPW',
        ),
        migrations.AlterField(
            model_name='creative',
            name='password',
            field=models.CharField(max_length=150),
        ),
    ]
