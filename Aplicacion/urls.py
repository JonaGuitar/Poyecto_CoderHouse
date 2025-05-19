from django.urls import path
from . import views

app_name = "Aplicacion"

urlpatterns = [
    path('post_listar', views.post_listar, name='post_listar'),
]