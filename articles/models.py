from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


class Tag(models.Model):
    slug = models.SlugField('слаг', max_length=50, unique=True)
    label = models.CharField('категории', max_length=50)

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

class Article(models.Model):
    title = models.CharField('название статьи', max_length=200, db_index=True)
    slug = models.SlugField('слаг', unique=True, max_length=200)
    img = models.ImageField('картинка', upload_to='images/', null=True, blank=True)
    body = models.TextField('текст статьи', db_index=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail_url', kwargs={'slug': self.slug})
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('имя автора', max_length=50)
    text = models.CharField('текст комментария', max_length=200)
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.author

class State(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    views = models.IntegerField('количество просмотров', default=0)
    likes = models.IntegerField('количество лайков', default=0)
    