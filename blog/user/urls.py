from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    #path('add_article/', views.add_article, name='add_article'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]