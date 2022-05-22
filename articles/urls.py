from django.urls import path

from .views import *

urlpatterns = [
    path('', articles_list, name='articles_list_url'),
    path('article/<slug>/', article_detail, name='article_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/<slug>/', tag_detail, name ='tag_detail_url')
]