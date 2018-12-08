from django.shortcuts import render, HttpResponse, redirect
from pymongo import MongoClient
from .forms import *
from .models import *

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    iterador = restaurantes.find().limit(10)
    context = {
        "lista": list(iterador)
    }
    return render(request, 'test.html', context)

def add_plato(request):
    if request.method == "POST":
        form = PlatoForm(request.POST)
        if form.is_valid():
            plato = form.save(commit=False)
            plato.save()
            mensaje = "Plato añadido"
        else:
            mensaje = "Error al crear el plato"
        context = {
            "mensaje": mensaje
        }
        return render(request, 'respuesta_formulario.html', context)
    else:
        form = PlatoForm()
        return render(request, 'add_plato.html', {'form': form})

