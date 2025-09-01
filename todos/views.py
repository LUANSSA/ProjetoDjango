from django.shortcuts import render
from django.views.generic import ListView, CreateView

# Create your views here.

from .models import Todo

def home(request):
    return render(request, "todos/home.html")

# def todo_list(request):
    
#     # Objeto
#     todos = Todo.objects.all()
#     # String
#     nome = "Luan"
#     # Lista
#     alunos = ["Caio Alexandre", "Marcelo Novaes", "Monique Alencar", "Gabriel Alexandria", "Luan Souza"]

#     return render(request, "todos/todo_list.html", {"nome": nome, "alunos": alunos, "todos": todos})

# Lista de tarefas
class ViewTodoList(ListView):
    model = Todo


# Criar tarefa
class ViewTodoCreate(CreateView):
    model = Todo
    # Formulário
    fields = ["title", "deadline"],
    success_url = "todo_list"
