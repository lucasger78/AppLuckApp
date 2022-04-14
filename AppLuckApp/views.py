from django.shortcuts import render
from django.http import HttpResponse
from AppLuckApp.models import Curso

#Create your views here.
def curso(self):
     curso = Curso(nombre = "Python", camada = "11111")
     curso.save()
    
     documento = f"El curso es de {curso.nombre}, y la comisión es la {curso.camada}"
    
     return HttpResponse(documento)