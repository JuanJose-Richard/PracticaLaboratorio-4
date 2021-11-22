from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Persona

def index(request):
    personas = Persona.objects.order_by('nombre')
    context = {
        'titulo_pagina': 'Lista de Personas',
        'lista_personas': personas,
        
        }
    #salida = ', '.join([p.nombre for p in persona])
    return render(request, 'personas.html',context)

def detail (request, persona_id):
    persona = Persona.objects.get(pk=persona_id)
    context = {
        'titulo_pagina': 'Ver Persona',
        'persona': persona,
        
        }
    return render(request, 'persona.html', context)
