from django.db.models import fields
from .models import Post
from django import forms
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','date_posted', 'author', 'image','payment_for','ngo_name']