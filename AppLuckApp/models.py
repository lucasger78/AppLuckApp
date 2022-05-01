from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    contenido = models.CharField(max_length=3000)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} Titulo: {self.titulo} Subtitulo: {self.subtitulo} Autor: {self.autor} {self.contenido} Fecha de publicación: {self.fecha}"
    
    
class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcarpeta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)