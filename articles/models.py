from django.db import models

from django.urls import reverse
from django.utils.text import slugify
from time import time

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
        self.slug = gen_slug(self.label)
        super().save(*args, **kwargs)

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
        return reverse('article_update_url',kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('article_delete_url',kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    
class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField('имя автора', max_length=50)
    text = models.CharField('текст комментария', max_length=200)
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.author

class State(models.Model):
    article = models.ForeignKey(Article, related_name='states', on_delete=models.CASCADE, verbose_name='статья')
    views = models.IntegerField('количество просмотров', default=0)
    likes = models.IntegerField('количество лайков', default=0)

    def __str__(self):
        return str(self.likes)
    