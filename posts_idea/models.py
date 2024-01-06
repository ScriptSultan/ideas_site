from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.


class Users(models.Model):
    user_id_tel = models.IntegerField()
    user_town = models.CharField(max_length=100)
    user_age = models.IntegerField()

    def __str__(self):
        return self.user_id


class Category(models.Model):
    name_cat = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name_cat


class Places(models.Model):
    name_place = models.CharField(max_length=100, verbose_name="Название")
    place_town = models.CharField(max_length=100, verbose_name="Город")
    place_description = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена", null=True, default=None)
    character_place = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория", related_name='get_category',
        null=True, default=None
    )
    one_photo_place = models.ImageField(upload_to='photo_ideas/', verbose_name="Фото")
    url_place = models.TextField(verbose_name="Ссылка на место")
    url_site = models.TextField(verbose_name="Ссылка на сайт")
    slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_place)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name_place