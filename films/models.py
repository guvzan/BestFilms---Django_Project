from django.db import models

from users.models import CustomUser

class Film(models.Model):
    """Фільм"""
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='images')
    text = models.TextField()
    duration = models.IntegerField()
    url = models.URLField()
    country = models.ForeignKey('Tag', related_name='country', on_delete=models.PROTECT)
    tag1 = models.ForeignKey('Tag', related_name='tag1', on_delete=models.PROTECT, blank=True, null=True)
    tag2 = models.ForeignKey('Tag', related_name='tag2', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Тег"""
    title = models.CharField(max_length = 20)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Коментар до фільму"""
    film = models.ForeignKey('Film', on_delete=models.PROTECT)
    title = models.CharField(max_length = 30, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    likes = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=CustomUser.objects.get(id=1).id)

    def __str__(self):
        return self.title

    def like(self):
        """Збільшити к-ть лайків на 1"""
        self.likes += 1
        self.save()

class BlogPost(models.Model):
    """Допис у блозі"""
    film = models.ForeignKey('Film', on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=CustomUser.objects.get(id=1).id)
    text = models.TextField(verbose_name='Текст')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]
