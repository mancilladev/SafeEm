from django.contrib import admin
from .models import Tarea, Empleado, Comentario, SubComentario

# Register your models here.
admin.site.register(Tarea)
admin.site.register(Empleado)
admin.site.register(Comentario)
admin.site.register(SubComentario)
