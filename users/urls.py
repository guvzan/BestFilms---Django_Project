from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    #Автентифікація
    path('', include('django.contrib.auth.urls')),

    #Реєстрація
    path('register/', views.register, name='register'),

    #Сторінка користувача
    path('account/<int:user_id>/', views.account, name='account'),

    #Лайкнути пост на сторінці
    path('account/<int:user_id>/<int:post_id>/', views.add_acc_like, name='acclike'),

    #Поділитись постом
    path('share/<int:post_id>/<int:user_id>/', views.share, name='share'),

    #Написати пост на сторінці
    path('account/add_post/<int:user_id>/', views.create_page_post, name='create_page_post'),
]