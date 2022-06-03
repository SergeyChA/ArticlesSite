from django.urls import path

from .views import *

urlpatterns = [
    path('', articles_list, name='articles_list_url'),
    path('article/create/', ArticleCreate.as_view(), name ='article_create_url'),
    path('article/<str:slug>/', ArticleDetail.as_view(), name='article_detail_url'),
    path('article/<str:slug>/update/', ArticleUpdate.as_view(), name='article_update_url'),
    path('article/<str:slug>/delete/', ArticleDelete.as_view(), name='article_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name ='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name ='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
]