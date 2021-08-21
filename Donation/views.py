from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import PostForm


def index(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }
    return render(request, 'donation/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'donation/register.html',context)

def donate(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }
    return render(request, 'donation/donate.html',context)

def payment(request):
    return render(request, 'donation/payment.html')

def payment_success(request):
    return render(request, 'donation/payment_success.html')

def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
    }

    
    return render(request, 'donation/add_post.html', context)

def about_us(request):
    return render(request, 'donation/about_us.html')

def users(request):
    return render(request, 'donation/users_login.html')