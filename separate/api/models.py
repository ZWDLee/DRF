from django.db import models

# Create your models here.

class User(models.Model):
    url = models.CharField(max_length=80, blank=False, default='')
    username = models.CharField(max_length=20, blank=False, default='')
    email = models.EmailField(blank=False)

class Books(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30, blank=True, null=True)