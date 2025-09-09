from django.db import models

# Create your models here.

class Todo(models.Model):
    # Titulo da tarefa
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    # Data de criação
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    # Data de entrega
    deadline = models.DateField(verbose_name="Data de Entrega", null=False, blank=False)
    # Data de finalização
    finished_at = models.DateTimeField(null=True)

