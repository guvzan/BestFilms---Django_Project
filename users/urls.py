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

    #Сторінка з повідомленнями
    path('account/messages/<int:user_id>/<int:default_id>/', views.show_messages, name='show_messages'),

    #Позначити повідомлення як прочитане
    path('account/messages/readed/<int:user_id>/<int:message_id>/', views.mark_as_read, name='mark_as_read'),

    #Видалити повідомлення
    path('account/messages/delete/<int:user_id>/<int:message_id>/', views.delete_message, name='delete_message'),

    #Відстежувати профіль користувача
    path('account/save/<int:to_save_id>/<int:saver_id>/', views.save_acc, name='save_acc'),

    #Профілі, що відстежуються
    path('account/saved_profiles/<int:user_id>/', views.saved_accs, name='saved_accs'),

    #Редагувати профіль
    path('account/<int:user_id>/edit/', views.edit_acc, name='edit_acc'),
]