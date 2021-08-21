from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images',default = 'default.jpg' )
    payment_for = models.CharField(max_length=200)
    ngo_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

