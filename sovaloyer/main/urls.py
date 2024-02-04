from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('orel/<int:count>', views.orel_reshka),
    path('random/<int:count>', views.random_n),
    path('rubik/<int:count>', views.rubik),
    path('authors/', views.author_view),
    path('articles/', views.articles_view),
    path('author_article/<int:author_id>', views.author_article, name='author_article'),
    path('article/<int:article_id>', views.article, name='article'),
    path('game/', views.choose_game, name='choose_game'),
    path('add-author/', views.author_add, name='add_author'),
    path('add-article/', views.add_article, name='add_article'),
]
