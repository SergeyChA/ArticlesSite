from dataclasses import field
from django import forms
from .models import Article, Tag, Comment
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['label']

        widgets = {'label': forms.TextInput(attrs={'class': 'form-control'})}

    

    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'tags', 'img']

        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'body': forms.Textarea(attrs={'class': 'form-control'}),
                   'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),         
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

        widgets = {'author': forms.TextInput(attrs={'class': 'form-control'}),
                   'text': forms.Textarea(attrs={'class': 'form-control'})
        }


    
        
