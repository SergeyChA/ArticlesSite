from django.shortcuts import render

from .models import Article, Tag

def articles_list(request):
    articles = Article.objects.order_by('-pub_date')
    return render(request, 'articles/main_page.html', context={'articles': articles})

def article_detail(request, slug):
    article = Article.objects.get(slug__iexact=slug)
    return render(request, 'articles/article_page.html', context={'article': article})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'articles/tags_page.html', context={'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'articles/tag_page.html', context={'tag': tag})
    