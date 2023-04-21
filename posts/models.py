from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_post')
    select1_content = models.TextField()
    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_post')
    select2_content = models.TextField()
    image_1 = models.ImageField(blank=True)
    image_2 = models.ImageField(blank=True)
    
class Comment_post(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Emote_post(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=10)