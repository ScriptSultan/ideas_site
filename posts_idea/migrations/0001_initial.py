# Generated by Django 5.0.1 on 2024-01-04 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_cat', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id_tel', models.IntegerField()),
                ('user_town', models.CharField(max_length=100)),
                ('user_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_place', models.CharField(max_length=100, verbose_name='Название')),
                ('place_town', models.CharField(max_length=100, verbose_name='Город')),
                ('place_description', models.TextField(verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('one_photo_place', models.ImageField(upload_to='photos_ideas', verbose_name='Фото')),
                ('url_place', models.TextField(verbose_name='Ссылка на место')),
                ('url_site', models.TextField(verbose_name='Ссылка на сайт')),
                ('slug', models.SlugField(max_length=100)),
                ('character_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts_idea.category', verbose_name='Категория')),
            ],
        ),
    ]
