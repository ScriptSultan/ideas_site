# Generated by Django 5.0.1 on 2024-01-04 21:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_idea', '0003_alter_places_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='character_place',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_category', to='posts_idea.category', verbose_name='Категория'),
        ),
    ]
