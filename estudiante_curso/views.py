from django.shortcuts import render, redirect
from .models import EstudianteCurso

def Estudiante_Curso(request):
    estudiante_curso = EstudianteCurso.objects.all()
    return render(request, 'lista_est_cur.html', {
        'title': 'Relacion estudiantes y curso',
        'estudiantes_cursos': estudiante_curso,
    })