from dataclasses import fields
import email
from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from AppLuckApp.forms import PostFormulario, UserEditForm, UserRegisterForm
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

from AppLuckApp.models import Avatar, Post

def avatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, {"url":avatares[0].imagen.url})

def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "AppLuckApp/index.html")



def about(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "AppLuckApp/about.html")
    

#------1 - CREATE -------
def postFormulario(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if request.method == "POST":
        miFormulario = PostFormulario(request.POST)                                                                     

        print(miFormulario)
        
        if miFormulario.is_valid:
         
            informacion = miFormulario.cleaned_data

            tituloNuevo = informacion['titulo']
            tituloChecker = Post.objects.filter(titulo__contains = tituloNuevo)

            if tituloChecker.exists():
                return render(request, "AppLuckApp/postFormulario.html", {"mensaje":"Ya hay un post con el mismo título !","miFormularioBlog":miFormulario})
            else:
                post = Post(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], autor=informacion['autor'], contenido=informacion['contenido'], fecha=informacion['fecha']) 
                post.save()                                                                                
                return render(request, "AppLuckApp/postFormulario.html", {"mensaje":"Post creado!","miFormularioBlog":miFormulario})                                                                
    else:
        miFormulario = PostFormulario()     
                                                                                                                            
    return render (request, "AppLuckApp/postFormulario.html", {"miFormularioBlog":miFormulario})



#------2 - READ -------
def leerPost(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    post = Post.objects.all()
    
    contexto= {"post":post} 
    
    return render(request, "AppLuckApp/leerpost.html", contexto)


#------3 - UPLOAD -------   

def editarPost(request, post_titulo):
    avatares = Avatar.objects.filter(user=request.user.id)
    post = Post.objects.get(titulo=post_titulo)
    
    
    if request.method == "POST":

        miFormulario = PostFormulario(request.POST)                                                                     

        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            tituloNuevo = informacion['titulo']
            tituloChecker = Post.objects.filter(titulo__contains = tituloNuevo)

            if tituloChecker.exists():
                return render(request, "AppLuckApp/editarPost.html", {"mensaje":"Ya hay un post con el mismo título ! Si no quieres editar, vuelve a la página de blogs","miFormularioEditPost":miFormulario})
            else:
                post.titulo = informacion['titulo']
                post.subtitulo = informacion['subtitulo']
                post.autor = informacion['autor']
                post.contenido = informacion['contenido']
                post.fecha = informacion['fecha']
        
                post.save()                                                                               
                return render(request, "AppLuckApp/editarPost.html", {"mensaje":"Post modificado!","miFormularioEditPost":miFormulario})                                                                     
    else:  
        
        miFormulario = PostFormulario(initial={'titulo':post.titulo, 'subtitulo':post.subtitulo, 'autor':post.autor, 'contenido':post.contenido, 'fecha':post.fecha})
        
    return render(request, "AppLuckApp/editarPost.html", {"miFormularioEditPost":miFormulario, "post":post})



#------4 - DELETE -------  
def eliminarPost(request, post_titulo):
    
    post = Post.objects.get(titulo=post_titulo)
    post.delete()
    
    #vuelvo al menú
    post = Post.objects.all()
    
    contexto= {"post":post} 
    
    return render(request, "AppLuckApp/leerPost.html", contexto)





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



#-------------EDITAR USUARIO-------------

@login_required
def editarPerfil(request):
    avatares = Avatar.objects.filter(user=request.user.id)    
    usuario = request.user

    if request.method == 'POST':

        myForm = UserEditForm(request.POST)

        if myForm.is_valid:

            informacion =  myForm.cleaned_data['username']
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()
            
            return render(request, "AppLuckApp/index.html")  
    else:
        
         myForm = UserEditForm(initial={'email':usuario.email,'last_name':usuario.last_name,'first_name':usuario.first_name})
    
    return render(request, "AppLuckApp/editarPerfil.html", {"miFormularioEditPerfil": myForm, "usuario":usuario})


def buscar(request):
    return render (request,'AppLuckApp/buscarPost.html')

def busqueda(request):
    if request.method == 'POST':
        query = request.POST['query']
        listapost = Post.objects.filter(titulo__contains = query)

        return render(request, 'AppLuckApp/resultadoBusqueda.html',{'query':query,'leerPost':listapost})
    else:
        return render(request, 'AppLuckApp/resultadoBusqueda.html')



