import csv
import os
from pprint import pprint

from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from posts_idea.models import Places


# Create your views here.

def all_posts(request):
    places_posts = Places.objects.all()
    context = {'places_posts': places_posts}
    return render(request, 'catalog.html', context)

def post(request, slug):
    places_slug = Places.objects.filter(slug=str(slug))
    template = 'product.html'
    context = {'places': places_slug}
    return render(request, template, context)






#Для нескольких страниц или пагинации
# def bus_stations(request):
#     page_num = int(request.GET.get('page', 1))
#     pagi = Paginator(lst_read, 10)
#     lala = pagi.get_page(page_num)
#     context = {
#         'bus_stations': lala,
#         'page': lala,
#     }
#     return render(request, 'ideas.html', context)






#тренеровка
# from django.views.generic import View
#
# class ImageView(View):
#     def get(self, request, image_path):
#         image_path = os.path.join(settings.MEDIA_ROOT, image_path)
#         with open(image_path, 'rb') as f:
#             return HttpResponse(f.read(), content_type='image/jpeg')

