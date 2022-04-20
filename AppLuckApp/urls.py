from django.urls import path
from AppLuckApp import views 
#from AppLuckApp.views import cursoFormulario

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('curso', views.curso, name='Curso'),
    path('profesor', views.profesor, name='Profesor'),
    path('estudiante', views.estudiante, name='Estudiante'),
    path('entregable', views.entregable, name='Entregable'),
    path('cursoFormulario', views.cursoFormulario, name='CursoFormulario'),
    path('profesorFormulario', views.profesorFormulario, name='profesorFormulario'),
    path('buscar/', views.buscar),
]