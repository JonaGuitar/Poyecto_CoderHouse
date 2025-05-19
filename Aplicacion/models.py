from django.db import models

# Create your models here.
class Post(models.Model): 
    marca = models.CharField(max_length=100)
    modelo = models.TextField()
    pais = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

        
    def __str__(self):
        return self.marca