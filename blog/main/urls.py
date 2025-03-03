from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_article/', views.add_article, name='add_article'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('article/<int:article_id>/delete/', views.delete_article, name='delete_article'),
]

