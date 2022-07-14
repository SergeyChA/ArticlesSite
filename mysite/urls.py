"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from articles.API.views import ArticlesDetailView, ArticlesListView


from .views import redirect_articles





urlpatterns = [
    path('', redirect_articles),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('api/articles/auth/', include('rest_framework.urls')),
    path('api/articles/', ArticlesListView.as_view()),
    path('api/articles/<int:pk>', ArticlesDetailView.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
   
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

