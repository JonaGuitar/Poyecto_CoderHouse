from django.urls import path
from . import views

app_name = "Aplicacion"

urlpatterns = [
    path('post_listar', views.post_listar, name='post_listar'),
    #path('create-category/', views.create_category, name='create_category'),
    #path('create-post/', views.create_post, name='create_post'),
    #path('search/', views.search_post, name='search_post'),
]