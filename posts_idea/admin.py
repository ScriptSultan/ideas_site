from django.contrib import admin

from posts_idea.models import Places, Category


# Register your models here.


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_place', 'place_description', 'character_place', 'price', 'one_photo_place', 'url_site', 'slug']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_cat']