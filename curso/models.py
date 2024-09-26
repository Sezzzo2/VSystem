from django.db import models
from persona.models import Persona

class curso(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad_max=models.CharField(max_length=100)
    profesor_id=models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} - {self.profesor_id}'
    
    class Meta:
        db_table = 'cursos'
