from django.shortcuts import render, HttpResponse, redirect
from pymongo import MongoClient
from .forms import *
from .models import *
import json
# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    iterador = restaurantes.find().limit(10)
    context = {
      "lista": list(iterador)
    }
    return render(request, 'test.html', context)

def lista_jQuery(request):
    rest_total = 109
    iterador = restaurantes.find().limit(rest_total)
    rest_por_pag = 10
    num_paginas = rest_total % rest_por_pag

    if num_paginas == 0:
        paginador = 0 
    else:
        paginador = range(0, int(rest_total / rest_por_pag + 1))

    context = {
        "lista": list(iterador),
        "paginador": paginador,
        "rest_por_pag": rest_por_pag
    }
    
    return render(request, 'restaurantes_jQuery.html', context)

def lista_ajax(request):

    iterador = restaurantes.find().limit(10)

    rest_por_pag = 10
    num_paginas = iterador.count() % rest_por_pag

    if num_paginas == 0:
        paginador = range(1, int(iterador.count() / rest_por_pag + 1))
    else:
        paginador = range(1, int(iterador.count() / rest_por_pag + 2))


    context = {
        "lista": list(iterador),
        "paginador": paginador
    }
    
    return render(request, 'restaurantes_ajax.html', context)

def restajax(request):
  pag = int(request.GET.get('pagina',''))
  pag = pag - 1

  rest_por_pag = 10

  rest = restaurantes.find().limit(10) 
  
  inicio = rest_por_pag * pag
  fin = inicio
  
  rest_para_mostrar = int(rest.count() % rest_por_pag);

  rest_aux = []

  if pag == int(rest.count() / rest_por_pag):
      fin += rest_para_mostrar
      for i in range(0, rest_para_mostrar):
          rest_aux.append([0])
  else:
      fin += rest_por_pag
      for i in range(0,rest_por_pag):
          rest_aux.append([None])
          
  i=0;
  for item in rest[inicio:fin]:
      rest_aux[i][0]=item['name']
      i+=1;

  return HttpResponse(json.dumps({'restaurantes': rest_aux}), content_type="application/json")


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

