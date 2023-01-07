from django.urls import path

from . import views

app_name = 'films'
urlpatterns = [
    #Головна сторінка
    path('', views.index, name='index'),

    #Сторінка з детальнішим описом фільмів
    path('more', views.more, name='more'),

    #Сторінка з детальнішим описом фільмів
    path('film/<int:film_id>', views.film, name='film'),

    #Сторінка для додавання тега
    path('new_tag', views.new_tag, name='new_tag'),

    #Сторінка для додавання фільму
    path('new_film', views.new_film, name='new_film'),

    #Додавання лайку до коментаря
    path('film/<int:film_id>/<int:comment_id>', views.add_like, name='add_like'),

    #Сторінка рандомного фільму
    path('film/', views.random_film, name='random_film'),

    #Сторінка блогу
    path('blog/', views.blog, name='blog'),


]