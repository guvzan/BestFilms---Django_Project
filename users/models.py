from django.db import models
from django.contrib.auth.models import AbstractUser

def default_post_list():
    return dict(id = [], saved_accs=[])

def default_list_of_likers():
    return dict(liked = [], saved = [])

def default_messages():
    return dict(unseen = [], seen =[], send = [])

class CustomUser(AbstractUser):
    """Кастомний користувач"""
    status = models.CharField(max_length=100, default='---', verbose_name='Статус')
    dob = models.DateField(blank=True, null=True, default='1999-12-31', verbose_name='Дата народження')
    about = models.TextField(blank=True, null=True, default='---', verbose_name='Про себе')
    image = models.ImageField(upload_to='images/avatars', blank=True, null=True, verbose_name='Аватар')
    post_list = models.JSONField(blank=True, null=True, default=default_post_list, verbose_name='Список постів')


class PagePost(models.Model):
    """Запис на власній сторінці"""
    title = models.CharField(max_length=20, verbose_name='Заголовок')
    image = models.ImageField(blank=True, null=True, upload_to='images/post_images', verbose_name='Зображення')
    text = models.TextField(blank=True, null=True, verbose_name='Текст')
    likes = models.IntegerField(default=0, verbose_name='К-ть лайків')
    list_of_likers = models.JSONField(blank=True, null=True, default=default_list_of_likers, verbose_name='Хто лайкнув')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=CustomUser.objects.get(id=1).id, verbose_name='Автор')
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Дата додання')

    def __str__(self):
        return self.title

    def like(self):
        """Лайкнути пост"""
        self.likes += 1
        self.save()

    def unlike(self):
        """Забрати лайк з поста"""
        self.likes -= 1
        self.save()


class Inbox(models.Model):
    """Поштова скринька. Для повідомлень, наприклад"""
    messages = models.JSONField(blank=True, null=True, default=default_messages, verbose_name='Повідомлення')
    customuser = models.OneToOneField('CustomUser', on_delete=models.CASCADE, verbose_name='Кому належить')

    def __str__(self):
        return f"{self.customuser.username} inbox"


class Message(models.Model):
    """Повідомлення (як СМС)"""
    text = models.TextField()
    author = models.ForeignKey(CustomUser, verbose_name='Автор', related_name='author', on_delete=models.CASCADE, default=CustomUser.objects.get(id=1).id)
    receiver = models.ForeignKey(CustomUser, verbose_name='Отримувач', related_name='receiver', on_delete=models.CASCADE, default=CustomUser.objects.get(id=1).id)
    time = models.DateTimeField(auto_now_add=True, verbose_name='Час надсилання')

    def __str__(self):
        return self.text[:10]
