import os
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(default='media/default.jpg', upload_to='profile_pics')
    followers = models.ManyToManyField(User, blank=True, related_name='user_followers')

    def __str__(self):
        return f'{self.user.username} Profile'


    