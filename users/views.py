from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


from .forms import *
from .models import *

def register(request):
    """Реєстрація користувача"""
    if request.method != 'POST':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('films:index')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def account(request, user_id):
    """Сторінка користувача за ід"""
    user = CustomUser.objects.get(id=user_id)
    user_posts = []
    test_post = PagePost.objects.filter(id=1)
    if user.post_list:
        for id in user.post_list['id']:
            exact_post = PagePost.objects.filter(id=id)
            if exact_post:
                user_posts.insert(0, exact_post)
    context = {
        'accuser': user,
        'user_posts': user_posts
    }
    return render(request, 'users/account.html', context)


def add_acc_like(request, user_id, post_id):
    """Додати лайк"""
    post = PagePost.objects.get(id = post_id)
    post.like()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'films:index'))


def share(request, post_id, user_id):
    """Поділитись дописом"""
    post = PagePost.objects.get(id = post_id)
    user = CustomUser.objects.get(id = user_id)
    liked_list = post.list_of_likers['saved']
    saved_list = user.post_list['id']

    if int(user_id) not in liked_list:
        liked_list.append(user_id)
        post.save()

    if int(post_id) not in saved_list:
        saved_list.append(post_id)
        user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'films:index'))


def create_page_post(request, user_id):
    """Створити допис на сторінці"""
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'GET':
        form = PagePostForm(user_id=user_id)
    else:
        form = PagePostForm(request.POST, request.FILES, user_id=user_id)
        if form.is_valid():
            new_form = form.save()
            user.post_list['id'].append(new_form.id)
            user.save()
            return redirect('films:index')
    context = {
        'form': form
    }
    return render(request, 'users/add_acc_post.html', context)


