from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "todos/home.html")

def todo_list(request):
    return render(request, "todos/todo_list.html")