import email
from django.db.models import F, Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, CreateView
from django.http import JsonResponse
from django.urls import reverse

from .models import Article, Tag, State, Comment, Account
from .utils import ObjectUpdateMixin, ObjectDeleteMixin
from .forms import ArticleForm, RegisterForm, TagForm, CommentForm, LoginForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

from django.core.paginator import Paginator


class RegisterUser(View):
    def get(self, request):
        form =RegisterForm()
        return render(request, 'articles/register_page.html', context={'form': form})

    def post(self, request):
        if request.POST:
            bound_form = RegisterForm(request.POST)
            if User.objects.filter(email__iexact=request.POST['email']):
                messages.error(request, 'Такой email уже зарегистрирован')

            elif bound_form.is_valid():
                bound_form.save()
                messages.success(request, 'Вы зарегистрированы')
                return redirect('login_url')

            return render(request, 'articles/register_page.html', context={'form': bound_form})
        

class LoginUser(View):
    def get(self, request):
        form =LoginForm()
        return render(request, 'articles/login_page.html', context={'form': form})

    def post(self, request):
        if request.POST:
            bound_form = LoginForm(data=request.POST)

            if bound_form.is_valid():
                user = bound_form.get_user()
                login(request, user)
                return redirect('articles_list_url')
            
            messages.error(request, 'Введите правильный логин и пароль')
            return render(request, 'articles/login_page.html', context={'form': bound_form})

def account_user(request):
    return render(request, 'articles/account_page.html')

def logout_user(request):
    logout(request)
    return redirect('login_url')



def pagination(request, obj_list):
    paginator = Paginator(obj_list, 6)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_page = '?page={}'.format(page.previous_page_number())
    else:
        prev_page = ''
    
    if page.has_next():
        next_page = '?page={}'.format(page.next_page_number())
    else:
        next_page = ''

    context = {
        'page': page,
        'is_paginated': is_paginated,
        'prev_page': prev_page,
        'next_page': next_page
    }
    return context

def articles_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        articles = Article.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        articles = Article.objects.all()

    context = pagination(request, articles)
    context.update({'search_query': search_query})
    return render(request, 'articles/main_page.html', context=context)



class ArticleDetail(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug__iexact=slug)
        if not request.session.get(slug):
            article.states.update(views=F('views') + 1)
            request.session[slug] = slug
        form = CommentForm()

        obj_list = article.comments.all()
        context = pagination(request, obj_list)
        context.update({'article': article, 'form': form })

        return render(request, 'articles/article_page.html', context=context)

    def post(self, request, slug):
        article = get_object_or_404(Article, slug__iexact=slug)
        if request.POST.get('statistics') == 'like':
            article.states.update(likes=F('likes') + 1)
            likes = str(article.states.get().likes)    
            return JsonResponse({"likes": likes})

        bound_form = CommentForm(request.POST)
        if bound_form.is_valid():
            new_comment = bound_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
        return redirect(article)
        
        

class ArticleCreate(LoginRequiredMixin, View):
    raise_exception = True
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

class ArticleUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Article
    form_model = ArticleForm
    template = 'articles/article_update.html'
    raise_exception = True

class ArticleDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Article
    template = 'articles/article_delete.html'
    redirect_url = 'articles_list_url'
    raise_exception = True
 

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'articles/tags_page.html', context={'tags': tags})

class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)

        obj_list = tag.articles.all()
        context = pagination(request, obj_list) 
        context.update({'tag': tag})
        
        return render(request, 'articles/tag_page.html', context=context)
    
class TagCreate(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request):
        form = TagForm()
        return render(request, 'articles/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        
        return render(request, 'articles/tag_create.html', context={'form': bound_form})

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model =Tag
    form_model = TagForm
    template = 'articles/tag_update.html'
    raise_exception = True

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'articles/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception = True




    
   


    