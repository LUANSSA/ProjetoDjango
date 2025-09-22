"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse

from todos.views import ViewTodoList, home, ViewTodoCreate, ViewTodoUpdate, ViewTodoDelete, ViewTodoComplete

# HTTP Resquest
def PaginaTeste1(request):

    pagina = '''
        <h1>Olá Mundo</h1>
        <ul>
            <li>Home</li>
            <li>Sobre</li>
            <li>Contato</li>
        </ul>
    '''

    # HTTP Response
    return HttpResponse(pagina)

def PaginaTeste2(request):

    with open("teste.html", "r", encoding="utf-8") as item:
        pagina = item.read()
    
    return HttpResponse(pagina)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path("tarefas/", ViewTodoList.as_view()),
    path("tarefas/cadastrar/", ViewTodoCreate.as_view()),
    path("tarefas/alterar/<int:pk>", ViewTodoUpdate.as_view()),
    path("tarefas/excluir/<int:pk>", ViewTodoDelete.as_view()),
    path("tarefas/concluir/<int:pk>", ViewTodoComplete.as_view()),
    path("teste1/", PaginaTeste1),
    path("teste2/", PaginaTeste2)
]
