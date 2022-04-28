from django.db import models

# Create your models here.
class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    

class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email= models.EmailField()
    

class Profesor(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email= models.EmailField()
    profesion = models.CharField(max_length=40)
    
    # con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email} - Profesión: {self.profesion}"
    

class Entregable(models.Model):
    
    nombre = models.CharField(max_length=40)
    fehaDeEntrega = models.DateField()
    entregado= models.BooleanField()