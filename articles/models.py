from tabnanny import verbose
from django.db import models

from django.urls import reverse
from django.utils.text import slugify
from time import time
from django.contrib.auth.models import User

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Tag(models.Model):
    label = models.CharField('категория', max_length=50, db_index=True)
    slug = models.SlugField('URL', blank=True, max_length=50, unique=True)

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url',kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url',kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.label)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
   

class Article(models.Model):
    title = models.CharField('название статьи', max_length=200, db_index=True)
    slug = models.SlugField('URL', unique=True, blank=True, max_length=200)
    img = models.ImageField('картинка', upload_to='images/', null=True, blank=True)
    body = models.TextField('текст статьи', db_index=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles', verbose_name='категории')
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True, db_index=True)
    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('article_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('article_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, max_length=50, on_delete = models.CASCADE)
    text = models.CharField('текст комментария', max_length=200)
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True, db_index=True)
    author_avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.author

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        
class State(models.Model):
    article = models.ForeignKey(Article, related_name='states', on_delete=models.CASCADE, verbose_name='статья')
    views = models.IntegerField('количество просмотров', default=0)
    likes = models.IntegerField('количество лайков', default=0)

    def __str__(self):
        return str(self.likes)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'

class Account(models.Model):
    user = models.OneToOneField(User, related_name='accounts', verbose_name='имя пользователя', on_delete=models.CASCADE)
    avatar = models.ImageField('аватар', upload_to='avatars/', null=True, blank=True)
    likes_articles = models.TextField(blank=True, null=True)
    sex = models.CharField('пол', max_length=150, blank=True, null=True)
    age = models.CharField('возраст', max_length=150, blank=True, null=True)
    interests = models.CharField('интересы', max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    