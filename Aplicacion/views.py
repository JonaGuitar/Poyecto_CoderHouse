from django.shortcuts import render
from .models import Post

# Create your views here.
def post_listar(request):
    post_listar = Post.objects.all()
    return render(request, "Aplicacion/listar_vehiculos.html", context={"Posts": post_listar})