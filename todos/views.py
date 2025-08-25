from django.shortcuts import render

# Create your views here.

from .models import Todo

def home(request):
    return render(request, "todos/home.html")

def todo_list(request):
    
    # Objeto
    todos = Todo.objects.all()
    # String
    nome = "Luan"
    # Lista
    alunos = ["Caio Alexandre", "Marcelo Novaes", "Monique Alencar", "Gabriel Alexandria", "Luan Souza"]

    return render(request, "todos/todo_list.html", {"nome": nome, "alunos": alunos, "todos": todos})