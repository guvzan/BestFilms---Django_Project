from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
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


@login_required
def account(request, user_id):
    """Сторінка користувача за ід"""
    user = CustomUser.objects.get(id=user_id)
    inbox = Inbox.objects.filter(customuser=user_id)
    if not inbox:
        new_inbox = Inbox(customuser=user)
        new_inbox.save()
        inbox = Inbox.objects.filter(customuser=user_id)

    user_posts = []
    new_messages_count = len(inbox[0].messages['unseen'])

    user_posts = []
    test_post = PagePost.objects.filter(id=1)
    if user.post_list:
        for id in user.post_list['id']:
            exact_post = PagePost.objects.filter(id=id)
            if exact_post:
                user_posts.insert(0, exact_post)



    context = {
        'accuser': user,
        'user_posts': user_posts,
        'inbox': inbox,
        'new_messages_count': new_messages_count
    }
    return render(request, 'users/account.html', context)


@login_required
def add_acc_like(request, user_id, post_id):
    """Додати лайк"""
    post = PagePost.objects.get(id = post_id)
    if int(user_id) not in post.list_of_likers['liked']:
        post.list_of_likers['liked'].append(user_id)
        post.like()
    else:
        post.list_of_likers['liked'].remove(user_id)
        post.unlike()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'films:index'))


@login_required
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


@login_required
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


@login_required
def show_messages(request, user_id):
    """Показати повідомлення"""
    accuser = CustomUser.objects.get(id=user_id)
    inbox = Inbox.objects.get(customuser=user_id)
    unseen_messages = []
    seen_messages = []
    sent_messages = []

    for id in inbox.messages['unseen']:
        exact_message = Message.objects.filter(id=id)
        if exact_message:
            unseen_messages.insert(0, exact_message)

    for id in inbox.messages['seen']:
        exact_message = Message.objects.filter(id=id)
        if exact_message:
            seen_messages.insert(0, exact_message)

    for id in inbox.messages['send']:
        exact_message = Message.objects.filter(id=id)
        if exact_message:
            sent_messages.insert(0, exact_message)

    if request.method == 'GET':
        form = MessageForm(user_id=user_id)
    else:
        form = MessageForm(request.POST, user_id=user_id)
        print(form.is_valid())
        print(request.POST)
        if form.is_valid():
            new_message = form.save()
            inbox.messages['send'].append(new_message.id)
            receiver_inbox = Inbox.objects.get(id=request.POST['receiver'])
            receiver_inbox.messages['unseen'].append(new_message.id)
            inbox.save()
            receiver_inbox.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'films:index'))



    context = {
        'accuser': accuser,
        'inbox': inbox,
        'unseen_messages': unseen_messages,
        'seen_messages': seen_messages,
        'sent_messages': sent_messages,
        'form': form
    }
    return render(request, 'users/messages.html', context)


@login_required
def mark_as_read(request, user_id, message_id):
    """Позначити повідомлення як прочитане"""
    message = Message.objects.get(id=message_id)
    user = CustomUser.objects.get(id=user_id)
    inbox = Inbox.objects.get(customuser=user)
    inbox.messages['unseen'].remove(message_id)
    inbox.messages['seen'].append(message_id)
    inbox.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'films:index'))


@login_required
def delete_message(request, user_id, message_id):
    """Видалити повідомлення"""
    message = Message.objects.get(id=message_id)
    user = CustomUser.objects.get(id=user_id)
    inbox = Inbox.objects.get(customuser=user)

    for cat in inbox.messages:
        if int(message_id) in inbox.messages[cat]:
            print(cat)
            inbox.messages[cat].remove(message_id)
    inbox.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'films:index'))


@login_required
def save_acc(request, to_save_id, saver_id):
    """Відстежувати профіль користувача"""
    saver = CustomUser.objects.get(id=saver_id)
    if int(to_save_id) not in saver.post_list['saved_accs']:
        saver.post_list['saved_accs'].append(to_save_id)
        saver.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'films:index'))


@login_required
def saved_accs(request, user_id):
    """Список профілів, що відстежуються користувачем"""
    accuser = CustomUser.objects.get(id=user_id)
    profile_list = accuser.post_list['saved_accs']
    profiles = []
    for p in profile_list:
        profiles.append(CustomUser.objects.filter(id=p)[0])

    users = None
    if request.method == 'POST':
        form = SearchUserForm(request.POST)
        if form.is_valid():
            users = find_user(form.cleaned_data['username'])
    else:
        form = SearchUserForm()


    context = {
        'accuser': accuser,
        'profiles': profiles,
        'form': form,
        'users': users
    }
    return render(request, 'users/saved_accs.html', context)


def find_user(username):
    """Пошук користувача за іменем"""
    if username == '':
        return CustomUser.objects.filter(id=1)
    list_of_users = CustomUser.objects.filter(username__icontains=username)
    return list_of_users


