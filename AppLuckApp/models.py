from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    contenido = models.CharField(max_length=1000)
    fecha = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} Titulo: {self.titulo} Subtitulo: {self.subtitulo} Autor: {self.autor} {self.contenido} Fecha de publicación: {self.fecha}"