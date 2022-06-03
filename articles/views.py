from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.http import JsonResponse
from django.urls import reverse

from .models import Article, Tag
from .utils import ObjectUpdateMixin, ObjectDeleteMixin
from .forms import ArticleForm, TagForm, CommentForm

def articles_list(request):
    articles = Article.objects.order_by('-pub_date')
    return render(request, 'articles/main_page.html', context={'articles': articles})


class ArticleDetail(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug__iexact=slug)
        if not request.session.get(slug):
            article.states.update(views=F('views') + 1)
            request.session[slug] = slug
        form = CommentForm()
        return render(request, 'articles/article_page.html', context={'article': article, 'form':form})

    def post(self, request, slug):
        article = get_object_or_404(Article, slug__iexact=slug)
        if request.POST.get('statistics') == 'like':
            article.states.update(likes=F('likes') + 1)
            likes = str(article.states.get().likes)    
            return JsonResponse({"likes": likes}, status=200)

        bound_form = CommentForm(request.POST)
        if bound_form.is_valid():
            new_comment = bound_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
        return redirect(article)
        
        

class ArticleCreate(View):
    def get(self, request):
        form = ArticleForm()
        return render(request, 'articles/article_create.html', context={'form': form})

    def post(self, request):
        if request.FILES:
            bound_form = ArticleForm(request.POST, request.FILES)
        else:
            bound_form = ArticleForm(request.POST)

        if bound_form.is_valid():
            new_article = bound_form.save()
            new_article.states.create()
            return redirect(new_article)
        
        return render(request, 'articles/article_create.html', context={'form': bound_form})

class ArticleUpdate(ObjectUpdateMixin, View):
    model = Article
    form_model = ArticleForm
    template = 'articles/article_update.html'

class ArticleDelete(ObjectDeleteMixin, View):
    model = Article
    template = 'articles/article_delete.html'
    redirect_url = 'articles_list_url'
 

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'articles/tags_page.html', context={'tags': tags})

class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'articles/tag_page.html', context={'tag': tag})
    
class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'articles/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        
        return render(request, 'articles/tag_create.html', context={'form': bound_form})

class TagUpdate(ObjectUpdateMixin, View):
    model =Tag
    form_model = TagForm
    template = 'articles/tag_update.html'

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'articles/tag_delete.html'
    redirect_url = 'tags_list_url'




    
   


    