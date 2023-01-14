from django.db import models

from users.models import CustomUser

def default_list_of_likers():
    return dict(liked = [])

class Film(models.Model):
    """Фільм"""
    title = models.CharField(max_length = 100, verbose_name='Назва')
    image = models.ImageField(upload_to='images', verbose_name='Постер')
    text = models.TextField(verbose_name='Опис')
    duration = models.IntegerField(verbose_name='Тривалість у хв')
    url = models.URLField(verbose_name='Посилання на трейлер')
    country = models.ForeignKey('Tag', related_name='country', on_delete=models.PROTECT, verbose_name='Країна')
    tag1 = models.ForeignKey('Tag', related_name='tag1', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Тег 1')
    tag2 = models.ForeignKey('Tag', related_name='tag2', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Тег 2')

    def __str__(self):
        return self.title


class Tag(models.Model):
    """Тег"""
    title = models.CharField(max_length = 20, verbose_name='Назва тегу')

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Коментар до фільму"""
    film = models.ForeignKey('Film', on_delete=models.PROTECT, verbose_name='Фільм')
    title = models.CharField(max_length = 30, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    likes = models.IntegerField(default=0, verbose_name='К-ть лайків')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата додання')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=CustomUser.objects.get(id=1).id, verbose_name='Автор')
    list_of_likers = models.JSONField(blank=True, null=True, default=default_list_of_likers, verbose_name='Хто лайкнув')

    def __str__(self):
        return self.title

    def like(self):
        """Збільшити к-ть лайків на 1"""
        self.likes += 1
        self.save()

    def unlike(self):
        """Зменшити к-ть лайків на 1"""
        self.likes -= 1
        self.save()

    def check_if_liked(self, user_id):
        """Перевірити, чи користувач поставив лайк"""
        if int(user_id) in self.list_of_likers['liked']:
            return True
        else:
            return False

class BlogPost(models.Model):
    """Допис у блозі"""
    film = models.ForeignKey('Film', on_delete=models.CASCADE, verbose_name='Заголовок')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=CustomUser.objects.get(id=1).id, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата додання')

    def __str__(self):
        return self.text[:20]
