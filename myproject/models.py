from django.db import models
import datetime as dt 
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    bio = HTMLField()
    phone = models.IntegerField(max_length=10)
    user = models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True)

