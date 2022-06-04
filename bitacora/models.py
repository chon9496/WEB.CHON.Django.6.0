from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title        = models.CharField(max_length=150)
    content      = models.TextField()
    thumbnail    = models.ImageField()
    publish_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.title