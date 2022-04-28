from django.urls import path
from AppLuckApp import views 
#from AppLuckApp.views import cursoFormulario
from django.contrib.auth.views import LogoutView

import AppLuckApp


urlpatterns = [
    path('', views.inicio, name='Inicio'),

    path('login', views.login_request, name= "Login"),
    path('register', views.register, name= "Register"), 
    path('logout', LogoutView.as_view(template_name='AppLuckApp/index.html'), name= "logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),

    path('about', views.about, name='About'),
    path('blogs',views.blogs,name="Blogs"),
]
