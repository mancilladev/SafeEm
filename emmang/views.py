from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Empleado, Tarea, Comentario
from .forms import TareaForm, UserCreateForm, ComentarioForm, EmpleadoForm, TareaForm

def home(request):
    return render(request, 'emmang/home.html')

@login_required
def portal(request):
    empleados = Empleado.objects.all()
    tareas = Tarea.objects.all().order_by('-fecha')
    tarea_archivo = Tarea.objects.exclude(archivo='').order_by('-fecha')
    mi = request.user.empleado
    return render(request, 'emmang/portal.html', {'empleados':empleados,'tareas':tareas,'tarea_archivo':tarea_archivo,'mi':mi})

@login_required
def tareas(request):
    if request.method == 'POST':
        form = TareaForm(request.POST, request.FILES)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.creador = request.user.empleado
            tarea.fecha = timezone.now()
            tarea.save()
            message = tarea.tema
    else:
        form = TareaForm()
        message = False
    tareas = Tarea.objects.all().order_by('-fecha')
    return render(request, 'emmang/tareas.html', {'form':form,'message':message,'tareas':tareas})

@login_required
def tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    comentarios = Comentario.objects.filter(tarea=tarea)
    self_pk = request.user.empleado.pk
    can_edit = self_pk == tarea.creador.pk
    return render(request, 'emmang/tarea.html', {'tarea':tarea,'can_edit':can_edit,'self_pk':self_pk,'comentarios':comentarios})

@login_required
def tarea_editar(request, pk):
    if request.method == 'POST':
        ins = get_object_or_404(Tarea, pk=pk)
        form = TareaForm(request.POST, request.FILES, instance=ins)
        if form.is_valid():
            tarea = form.save()
    return redirect('emmang:tarea', pk=pk)

@login_required
def comentario(request, e_pk, t_pk):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            empleado = get_object_or_404(Empleado, pk=e_pk)
            tarea = get_object_or_404(Tarea, pk=t_pk)
            comentario = form.save(commit=False)
            comentario.empleado = empleado
            comentario.tarea = tarea
            comentario.fecha = timezone.now()
            comentario.save()
    return redirect('emmang:tarea', pk=t_pk)

@login_required
def empleados(request):
    message = False
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            empleado = Empleado.objects.create(usuario=user, puesto=form.cleaned_data["puesto"])
            empleado.save()
            message = user.username
    else:
        form = UserCreateForm()
    empleados = Empleado.objects.all()
    return render(request, 'emmang/empleados.html', {'form':form,'message':message,'empleados':empleados,'user':request.user})

@login_required
def perfil_personal(request):
    return redirect('emmang:perfil', pk=request.user.empleado.pk)

@login_required
def perfil_editar(request):
    if request.method == 'POST':
        perfil = request.user.empleado
        form = EmpleadoForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            empleado = form.save()
    return redirect('emmang:perfil_personal')

@login_required
def perfil(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    tareas = Tarea.objects.filter(creador=empleado).order_by('-fecha')
    comentarios = Comentario.objects.filter(empleado=empleado).order_by('-fecha')
    can_edit = request.user.empleado == empleado
    return render(request, 'emmang/perfil.html', {'empleado':empleado,'tareas':tareas,'comentarios':comentarios,'can_edit':can_edit})
