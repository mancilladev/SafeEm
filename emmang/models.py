from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class Empleado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=75)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='img/')

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return str(self.usuario)

class Tarea(models.Model):
    creador = models.ForeignKey('emmang.Empleado', related_name='tareas')
    tema = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField()
    archivo = models.FileField(upload_to='docs/', null=True, blank=True)

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.tema

class ComentarioAbstracto(models.Model):
    texto = models.TextField()
    fecha = models.DateTimeField()

    class Meta:
        abstract=True

    def __str__(self):
        return self.texto

class Comentario(ComentarioAbstracto):
    empleado = models.ForeignKey('emmang.Empleado', related_name='comentarios')
    tarea = models.ForeignKey('emmang.Tarea', related_name='comentarios')

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

class SubComentario(ComentarioAbstracto):
    empleado = models.ForeignKey('emmang.Empleado', related_name='subcomentarios')
    comentario = models.ForeignKey('emmang.Comentario', related_name='subcomentarios')

    class Meta:
        verbose_name = "SubComentario"
        verbose_name_plural = "SubComentarios"
