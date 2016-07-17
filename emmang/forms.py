from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Tarea, Empleado, Comentario

class TareaForm(forms.ModelForm):
    tema = forms.CharField()
    texto = forms.CharField(widget=forms.Textarea)
    archivo = forms.FileField(required=False)
    class Meta:
        model = Tarea
        fields = ['tema','texto','archivo']

class UserCreateForm(UserCreationForm):
    puesto = forms.CharField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['puesto','descripcion','imagen']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['tema','texto','archivo']
