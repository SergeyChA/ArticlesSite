from django.contrib import admin

from .models import Article, Tag, Comment, State, Account


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'label')
    list_display_links = ('id', 'label')
    search_fields = ('label',)
    prepopulated_fields = {'slug': ('label',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'pub_date')
    list_display_links = ('id', 'author')
    search_fields = ('author',)
    

class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'views', 'likes')
    list_display_links = ('id', 'article')
    search_fields = ('article',)
    
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sex', 'age', 'interests')
    list_display_links = ('id', 'user')
    search_fields = ('user',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Account, AccountAdmin)
