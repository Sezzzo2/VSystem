"""
URL configuration for VSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainApp.views import inicio, get_prueba
from persona.views import get_estudiantes, formulario_estudiante
from curso.views import get_curso, formulario
from estudiante_curso.views import Estudiante_Curso


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name= 'inicio'),
    path('Lista-estudiantes/',get_estudiantes, name='lista-estudiantes'),
    path('Hola-Prueba/',get_prueba,name='Hola-Mundo-Prueba'),
    path('Lista-cursos/',get_curso,name='lista-cursos'),
    path('cursos/agregar/', formulario, name='formulario_curso'),
    path('estudiantes/agregar/', formulario_estudiante, name='formulario_estudiante'),
    path('estudiantes-curso/', Estudiante_Curso, name='estudiante_curso'),
]
