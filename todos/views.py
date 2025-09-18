from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import date

# Create your views here.

from .models import Todo

def home(request):
    return render(request, "todos/home.html")

# Lista de tarefas
class ViewTodoList(ListView):
    model = Todo

# Criar tarefa
class ViewTodoCreate(CreateView):
    model = Todo
    # Formulário
    fields = ["title", "deadline"]
    success_url = "/tarefas"

# Alterar tarefa
class ViewTodoUpdate(UpdateView):
    model = Todo
    # Formulario
    fields = ["title", "deadline"]
    success_url = "/tarefas"

# Excluir tarefa
class ViewTodoDelete(DeleteView):
    model = Todo
    success_url = "/tarefas"


#
class ViewTodoComplete(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished_at = date.today()
        todo.save()
        return redirect("/tarefas")
