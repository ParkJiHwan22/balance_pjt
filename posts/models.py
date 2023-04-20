from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    choose1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='choose1_post')
    choose1_content = models.TextField()
    choose2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='choose2_post')
    choose2_content = models.TextField()
    image_1 = models.ImageField(blank=True)
    image_2 = models.ImageField(blank=True)
