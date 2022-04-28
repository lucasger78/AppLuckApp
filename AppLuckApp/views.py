from dataclasses import fields
import email
from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from AppLuckApp.models import Curso, Profesor
from AppLuckApp.forms import CursoFormulario, ProfesorFormulario, UserEditForm, UserRegisterForm
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

@login_required
def inicio(request):
    return render(request, "AppLuckApp/inicio.html")

def curso(request):
    return render(request, "AppLuckApp/curso.html")

def profesor(request):
    return render(request, "AppLuckApp/profesor.html") 

def estudiante(request):
    return render(request, "AppLuckApp/estudiante.html")

def entregable(request):
    return render(request, "AppLuckApp/entregable.html")

#-------FORMULARIOS--------

def cursoFormulario(request):
    
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)                                                                     

        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada']) 
            curso.save()                                                                                
            return render(request, "AppLuckApp/inicio.html")                                                                      
    else:
        miFormulario = CursoFormulario()     
                                                                                                                            
    return render (request, "AppLuckApp/curso.html", {"miFormulario":miFormulario})


#-------BUSCADOR--------
       
def buscar(request):
    if request.GET["camada"]:
        
        camada = request.GET['camada']
        print(camada)
        curso = Curso.objects.filter(camada__icontains=camada)
        print(curso)
        return render(request, "AppLuckApp/inicio.html", {"curso":curso, "camada":camada})
    
    else:
        
        respuesta = "No hay Datos"
        
    #return HttpResponse(respuesta)
    return render(request, "AppLuckApp/inicio.html", {"respuesta":respuesta})

#------1-CRUD CREATED-(C)------- 

def profesorFormulario(request):
    
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)                                                                     

        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion']) 
            profesor.save()                                                                                
            return render(request, "AppLuckApp/inicio.html")                                                                      
    else:
        miFormulario = ProfesorFormulario()     
                                                                                                                            
    return render (request, "AppLuckApp/profesorFormulario.html", {"miFormulario":miFormulario})
       
#------2-CRUD READ-(R)-------   

def leerProfesor(request):
    
    profesor = Profesor.objects.all()
    
    contexto= {"profesor":profesor} 
    
    return render(request, "AppLuckApp/leerProfesor.html", contexto)

#------3-CRUD EDITAR-(U)-------   

def editarProfesor(request, profesor_nombre):
    
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    
    
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)                                                                     

        print(miFormulario)
        
        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
            
            profesor.nombre = informacion['nombre'], 
            profesor.apellido= informacion['apellido'], 
            profesor.email=informacion['email'], 
            profesor.profesion=informacion['profesion'] 
            
            
            profesor.save()
            
                
                                                                               
            return render(request, "AppLuckApp/inicio.html")                                                                      
    else:  
        
        miFormulario=ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion})
        
    return render(request, "AppLuckApp/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})
        
     
#------4-CRUD DELETE-(D)-------   

def eliminarProfesor(request, profesor_nombre):
    
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    #vuelvo al menú
    profesor = Profesor.objects.all()
    
    contexto= {"profesor":profesor} 
    
    return render(request, "AppLuckApp/leerProfesor.html", contexto)    


class CursoList(LoginRequiredMixin, ListView):
    
    model = Curso   
    template_name = "AppLuckApp/curso_list.html"
    
class CursoDetalle(DetailView):
    
    model = Curso   
    template_name = "AppLuckApp/curso_detalle.html"
    
class CursoCreacion(CreateView):
    
    model = Curso   
    succes_url = "/AppLuckApp/curso/list"
    fields = ['nombre', 'camada']
    
class CursoUpdate(UpdateView):
    
    model = Curso   
    succes_url = "/AppLuckApp/curso/list"
    fields = ['nombre', 'camada']
    
class CursoDelete(DeleteView):
    
    model = Curso   
    succes_url = "/AppLuckApp/curso/list"
    
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
                       
                return render(request,"AppLuckApp/inicio.html",  {"mensaje":f"Bienvenido {usuario}"} )
            else:
                        
                return render(request,"AppLuckApp/inicio.html", {"mensaje":"Error, datos incorrectos"} )

        else:
                        
            return render(request,"AppLuckApp/inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"AppLuckApp/login.html", {'form':form} )

#-------------REGISTRAR------------

def register(request):
    
    if request.method == 'POST':
        
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppLuckApp/inicio.html", {"mensaje":"Usuario Creado :P"})
        
    
    else:
        
        form = UserRegisterForm()
        
    return render(request, "AppLuckApp/registro.html", {"form":form})

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
