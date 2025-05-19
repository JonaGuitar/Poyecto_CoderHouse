from django.shortcuts import render

# Create your views here.
def index (request):
    context = {"mensaje": "Bienvenido a mi página con Bootstrap y Django"} 
    return render(request, "Aplicacion/index.html", context)