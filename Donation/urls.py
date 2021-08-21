
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('donate', views.donate, name='donate'),
    path('payment', views.payment, name='payment'),
    path('payment_success', views.payment_success, name='payment_success'),
    path('add',views.create_post, name='post'),
    path('about', views.about_us, name='about'),
    path('users', views.users, name='users'),
]