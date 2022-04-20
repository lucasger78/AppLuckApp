import email
from django.shortcuts import render
from django.http import HttpResponse
from AppLuckApp.models import Curso, Profesor
from AppLuckApp.forms import CursoFormulario, ProfesorFormulario

#Create your views here.
# def curso(self):
#      curso = Curso(nombre = "Python", camada = "11111")
#      curso.save()
    
#      documento = f"El curso es de {curso.nombre}, y la comisión es la {curso.camada}"
    
#      return HttpResponse(documento)

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
                                                                                                                            
    return render (request, "AppLuckApp/profesor.html", {"miFormulario":miFormulario})


def buscar(request):
    
    if request.GET['camada']:
        
       # respuesta = f"Estoy buscando la camada nro: {request.GET['camada']}"
       
       camada = request.GET['camada']
       print(camada)
       curso = Curso.objects.filter(camada__icontains=camada)
       print(curso)
       return render(request, "AppLuckApp/inicio.html", {"curso":curso, "camada":camada})
   
    else:
       
       respuesta = "No enviaste datos"
       
    #return HttpResponse(respuesta)
    return render(request, "AppLuckApp/inicio.html", {"respuesta":respuesta})
       



        