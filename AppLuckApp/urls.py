from django.urls import path
from AppLuckApp import views 
#from AppLuckApp.views import cursoFormulario
from django.contrib.auth.views import LogoutView

import AppLuckApp


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('curso', views.curso, name='Curso'),
    path('profesor', views.profesor, name='Profesor'),
    path('estudiante', views.estudiante, name='Estudiante'),
    path('entregable', views.entregable, name='Entregable'),
    path('cursoFormulario', views.cursoFormulario, name='CursoFormulario'),
    path('profesorFormulario', views.profesorFormulario, name='profesorFormulario'),
    path('buscar/',views.buscar), 
    path('leerProfesor',views.leerProfesor, name="LeerProfesor"),
    path('eliminarProfesor/<profesor_nombre>/',views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    
    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    
    path('login', views.login_request, name= "Login"),
    path('register', views.register, name= "Register"), 
    path('logout', LogoutView.as_view(template_name='AppLuckApp/logout.html'), name= "logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
]