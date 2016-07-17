from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    tema = forms.CharField()
    texto = forms.CharField(widget=forms.Textarea)
    archivo = forms.FileField(required=False)
    class Meta:
        model = Tarea
        fields = ['tema','texto','archivo']
