# Generated by Django 3.1.7 on 2021-06-29 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_creator', '0013_auto_20210629_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creative',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
