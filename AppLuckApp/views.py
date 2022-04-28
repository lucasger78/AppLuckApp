from dataclasses import fields
import email
from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from AppLuckApp.forms import UserEditForm, UserRegisterForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.views import LogoutView
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "AppLuckApp/index.html")

def about(request):
    return render(request, "AppLuckApp/about.html")

def blogs(request):
    return render(request,"AppLuckApp/blogs.html")




#-------------REGISTRAR------------

def register(request):
    
    if request.method == 'POST':
        
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppLuckApp/registro.html", {"mensaje":"Usuario Creado! Ya puedes inciar sesión"})
    else:
        
        form = UserRegisterForm()
        
    return render(request, "AppLuckApp/registro.html", {"registerForm":form})




#-------------LOGIN-------------

def login_request(request):
    
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            
            if user is not None:
                login(request, user)
                       
                return render(request,"AppLuckApp/index.html",  {"mensaje":f"Bienvenido {usuario}"})
            else:
                        
                return render(request,"AppLuckApp/login.html", {"mensaje":"Error, datos incorrectos", "loginForm":form})

        else:
                        
            return render(request,"AppLuckApp/login.html" ,  {"mensaje":"Error, datos incorrectos", "loginForm":form})

    form = AuthenticationForm()

    return render(request,"AppLuckApp/login.html", {'loginForm':form} )



@login_required
def editarPerfil(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        miFormulario == UserEditForm(request.POST)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            
            return render(request, "AppLuckApp/inicio.htm")
        
    else:
        
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, "AppLuckApp/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})
