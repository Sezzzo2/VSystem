from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona
from .forms import PersonaForm

# Vista para listar estudiantes
def get_estudiantes(request):
    estudiantes = Persona.objects.filter(rol='Estudiante')
    return render(request, 'lista-estudiantes.html', {
        'title': 'Lista de estudiantes',
        'estudiantes': estudiantes
    })

# Vista para agregar nuevos estudiantes
def formulario_estudiante(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False)  # No guardar aún en la base de datos
            estudiante.rol = 'Estudiante'  # Asignar el rol predeterminado
            estudiante.save()  # Ahora guarda el estudiante
            return redirect('lista-estudiantes')  # Redirige a la lista de estudiantes después de guardar
    else:
        form = PersonaForm()

    return render(request, 'formulario_estudiante.html', {'form': form})

# Vista para editar estudiantes
def editar_estudiante(request, estudiante_id):
    estudiante_instance = get_object_or_404(Persona, id=estudiante_id)

    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=estudiante_instance)
        if form.is_valid():
            form.save()
            return redirect('lista-estudiantes')
    else:
        form = PersonaForm(instance=estudiante_instance)

    return render(request, 'formulario_estudiante.html', {'form': form})

# Vista para eliminar estudiantes
def eliminar_estudiante(request, estudiante_id):
    estudiante_instance = get_object_or_404(Persona, id=estudiante_id)
    estudiante_instance.delete()
    return redirect('lista-estudiantes')
