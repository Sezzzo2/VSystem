from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import curso

def get_curso(request):

    cursos = curso.objects.all().values()

    return render(request,'lista_cursos.html', {
        'title':'Lista de cursos',
        'cursos': cursos
    })
