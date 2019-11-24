from django.db import models
import datetime as dt 
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    bio = HTMLField()
    phone = models.PositiveIntegerField()
    profile_pic = models.ImageField(upload_to='images/' , default='images/smoke.jpeg')
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

class Post(models.Model):
    title =  models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    description = HTMLField()
    link = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
class Reviews(models.Model):
    title = models.CharField(max_length=50)
    review = models.TextField()
    design = models.PositiveIntegerField(default=0)
    usability = models.PositiveIntegerField(default=0)
    content = models.PositiveIntegerField(default=0)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    