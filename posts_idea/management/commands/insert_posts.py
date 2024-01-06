import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from posts_idea.models import Places, Category
import logging

logger = logging.getLogger(__name__)

photos_folder = os.path.join(settings.BASE_DIR, 'posts_idea', 'static', 'photo_ideas')
photos_list = os.listdir(photos_folder)


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        categor_list = ['антикафе', 'кафе', 'ресторан', 'прогулка', 'меропрятие', 'дома', 'кинотеатр']
        category_objects = {}
        for cat in categor_list:
            categories = Category.objects.filter(name_cat=cat)
            if categories.exists():
                category_objects[cat] = categories.first()
            else:
                category = Category(name_cat=cat)
                category.save()
                category_objects[cat] = category
        with open('ideas.csv', 'r', encoding='utf-8') as file:
            places = list(csv.DictReader(file))
        for place in places:
            category_name = place['category'].lower()
            category = category_objects.get(category_name)
            try:
                place['price'] = int(place['price'])
            except (ValueError, TypeError):
                place['price'] = 0

            if category:
                insert_phone_bd = Places(
                    name_place=place['name_place'], place_town=place['place'], price=place['price'],
                    character_place=category, place_description=place['place_description'],
                    url_place=place['url_place']
                )
                insert_phone_bd.save()

        for photo_name in photos_list:
            photo_path = os.path.join(photos_folder, photo_name)
            insert_phone_bd = Places(one_photo_place=f'photo_ideas/{photo_name}')
            insert_phone_bd.save()
            pass