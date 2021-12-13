from django.shortcuts import render

# Create your views here.

def bienvenida(request):
    return render(request, "inicio/index.html", {})

def contacto(request):
    contexto = {"Nombre":"Nare",
                "lista_numeros":[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],
                "Edad": 26
                }
    return render(request, "inicio/contacto.html", contexto)