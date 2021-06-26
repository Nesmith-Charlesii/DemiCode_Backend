# Generated by Django 3.1.7 on 2021-06-26 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content_creator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('header_image', models.ImageField(null=True, upload_to='', verbose_name='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='creative',
            name='confirmPW',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='videos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='content_creator.creative')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('anon_name', models.CharField(default='anonymous', max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='content_creator.blog')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='content_creator.creative')),
                ('likes', models.ManyToManyField(null=True, related_name='likes', to='content_creator.Creative')),
            ],
        ),
        migrations.CreateModel(
            name='Digital_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='images/')),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='content_creator.creative')),
            ],
        ),
        migrations.CreateModel(
            name='Code_Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('upload', models.ImageField(null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to='content_creator.creative')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='content_creator.creative'),
        ),
    ]
