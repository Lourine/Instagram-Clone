import os
from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse
from django.conf import settings


def get_image_path(instance, filename):
    return os.path.join('posts', str(instance.author), filename)


class Post(models.Model):
    photo = models.ImageField(upload_to='images/')
    caption = models.TextField(max_length=2200, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    location = models.CharField(max_length=30, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('insta-detail', kwargs={'pk': self.pk})

    def get_api_like_url(self):
        return reverse('insta-post_like_api', kwargs={"pk": self.pk})




class Comment(models.Model):
    post = models.ForeignKey('insta.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=2200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    def save(self, **kwargs):
        super().save()


# Notification model is used for three different types of notifications: like,
# comment, and follow notifications.
class Notification(models.Model):
    post = models.ForeignKey('insta.Post', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    liked = models.BooleanField(default=False, null=True)
    followed = models.BooleanField(default=False, null=True)
    date_posted = models.DateTimeField(null=True, blank=True)
3