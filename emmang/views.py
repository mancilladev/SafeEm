from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Empleado, Tarea
from .forms import TareaForm

def home(request):
    # print(request.get_full_path())
    return render(request, 'emmang/home.html')

@login_required
def portal(request):
    return render(request, 'emmang/portal.html')

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
    return render(request, 'emmang/tarea.html')

@login_required
def empleados(request):
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
    empleados = Empleado.objects.all()
    return render(request, 'emmang/empleados.html', {'form':form,'message':message,'empleados':empleados})

@login_required
def perfil(request):
    empleado = get_object_or_404(Empleado, pk=request.user.empleado.pk)
    tareas = Tarea.objects.filter(creador=empleado).order_by('-fecha')
    return render(request, 'emmang/perfil.html', {'empleado':empleado,'tareas':tareas})
