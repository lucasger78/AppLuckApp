from dataclasses import field, fields
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        #saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}



class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label='Modificar e-mail')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
        
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        #saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class PostFormulario(forms.Form):
    titulo = forms.CharField()
    subtitulo = forms.CharField()
    autor= forms.CharField()
    contenido = forms.CharField() 
    fecha = forms.DateField()