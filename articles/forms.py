from dataclasses import field
from enum import unique
from django import forms
from .models import Article, Tag, Comment, Account
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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
                   'tags': forms.SelectMultiple(attrs={'class': 'col-md-6 form-control'}),         
        }
    # Validator
    # def clean_title(self):
    #     title = self.cleaned_data['title'] 
    #     if title[0].isdigit():
    #         raise ValidationError('ERRRRRORRRR')
    #     return title

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control','rows': 5})}

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget= forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email', widget= forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget= forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget= forms.PasswordInput(attrs={'class': 'form-control'}))
   
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget= forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget= forms.PasswordInput(attrs={'class': 'form-control'}))

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['sex', 'age', 'interests', 'avatar']

        widgets = {'sex': forms.TextInput(attrs={'class': 'form-control'}),
                   'age': forms.NumberInput(attrs={'class': 'form-control'}),
                   'interests': forms.TextInput(attrs={'class': 'form-control'}),         
        }



        





    
        
