from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def test_template(request):
    iterador = restaurantes.find().limit(10)
    context = {
        "lista": list(iterador)
    }
    return render(request, 'test.html', context)