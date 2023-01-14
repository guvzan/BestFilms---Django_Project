import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def index(request):
    """Головна сторінка"""
    #Бойовики
    blockbusters = []
    blockbusters_id = Tag.objects.filter(title='Бойовик')
    if blockbusters_id:
        blockbusters = Film.objects.filter(tag1=blockbusters_id[0].id) | Film.objects.filter(tag2=blockbusters_id[0].id)

    # Комедії
    comedy = []
    comedy_id = Tag.objects.filter(title='Комедія')
    if comedy_id:
        comedy = Film.objects.filter(tag1=comedy_id[0].id) | Film.objects.filter(tag2=comedy_id[0].id)

    # Фантастика
    fantastyka = []
    fantastyka_id = Tag.objects.filter(title='Фантастика')
    if fantastyka_id:
        fantastyka = Film.objects.filter(tag1=fantastyka_id[0].id) | Film.objects.filter(tag2=fantastyka_id[0].id)

    films = Film.objects.filter()
    context = {
        'films': films[:4],
        'blockbusters': blockbusters[:4],
        'comedy': comedy,
        'fantastyka': fantastyka
    }
    return render(request, 'films/index.html', context)

def more(request):
    """Показати детальнішу інформацію"""
    films = Film.objects.filter().order_by('title')
    context = {
        'films': films
    }
    return render(request, 'films/film_list.html', context)

def film(request, film_id):
    """Конкретний фільм"""
    film = Film.objects.get(id=film_id)
    comments = Comment.objects.filter(film=film_id).order_by('-likes')

    #Отримати нік користувача
    user_id = None
    accuser = None
    if request.user.is_authenticated:
        user_id = request.user.id
        accuser = CustomUser.objects.get(id=user_id)

    if str(request.user) == 'AnonymousUser':
        form = None
    else:
        if request.method != 'POST':
            form = CommentForm(film_id=film_id, user_id=user_id)
        else:
            form = CommentForm(request.POST, film_id=film_id, user_id=user_id)
            if form.is_valid():
                form.save()
                return redirect('films:film', film_id)

    context = {
        'film': film,
        'comments': comments,
        'form': form,
        'accuser': accuser
    }
    return render(request, 'films/chosen_film.html', context)


@login_required
def new_tag(request):
    """Додати новий тег"""
    if request.method != 'POST':
        form = TagForm()
    else:
        form = TagForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('films:new_tag')

    tags = Tag.objects.all().order_by('title').values()

    context = {
        'form': form,
        'tags': tags
    }
    return render(request, 'films/new_tag.html', context)


@login_required
def new_film(request):
    """Додати новий фільм"""
    if request.method != 'POST':
        form = FilmForm()
    else:
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('films:new_film')

    context = {'form': form}
    return render(request, 'films/new_film.html', context)


@login_required
def add_like(request, film_id, comment_id, user_id):
    """Додати лайк"""
    comment = Comment.objects.get(id = comment_id)
    if int(user_id) not in comment.list_of_likers['liked']:
        comment.list_of_likers['liked'].append(user_id)
        comment.like()
    else:
        comment.list_of_likers['liked'].remove(user_id)
        comment.unlike()
    return redirect('films:film', film_id)


def random_film(request):
    """Показати рандомний фільм"""
    films = Film.objects.all()
    last_id = len(films)
    try:
        return redirect('films:film', random.randint(1, last_id))
    except:
        return redirect('films:film', 1)


def blog(request):
    """Сторінка блогу"""
    texts = BlogPost.objects.all()
    len_texts = len(texts)
    posts = {
        'texts': texts,
        'colors': [145 + i for i in range(len_texts)],
        'ids': [i for i in range(len_texts)]
    }
    context = {
        'posts': posts
    }
    return render(request, 'films/blog.html', context)








