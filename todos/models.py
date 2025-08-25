from django.db import models

# Create your models here.

class Todo(models.Model):
    # Titulo da tarefa
    title = models.CharField(max_length=100, null=False, blank=False)
    # Data de criação
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    # Data de entrega
    deadline = models.DateTimeField(null=False, blank=False)
    # Data de finalização
    finished_at = models.DateTimeField(null=True)

