from django.db import models
from django.contrib.auth.models import AbstractUser

def default_post_list():
    return dict(id = [])

def default_list_of_likers():
    return dict(liked = [], saved = [])

class CustomUser(AbstractUser):
    """Кастомний користувач"""
    status = models.CharField(max_length=100, default='---')
    dob = models.DateField(blank=True, null=True, default='1999-12-31')
    about = models.TextField(blank=True, null=True, default='---')
    image = models.ImageField(upload_to='images', blank=True, null=True)
    post_list = models.JSONField(blank=True, null=True, default=default_post_list)


class PagePost(models.Model):
    """Запис на власній сторінці"""
    title = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True, upload_to='images/post_images')
    text = models.TextField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    list_of_likers = models.JSONField(blank=True, null=True, default=default_list_of_likers)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=CustomUser.objects.get(id=1).id)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def like(self):
        """Лайкнути пост"""
        self.likes += 1
        self.save()
