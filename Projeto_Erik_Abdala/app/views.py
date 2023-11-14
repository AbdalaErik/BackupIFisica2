from django.shortcuts import render
from . models import *

# Create your views here.

def area(request):

    areas = {
        'areas':Area.objects.all()
    }

    return render(request, 'exibicao/area.html', areas)

def subarea(request):

    subareas = {
        'subareas':Subarea.objects.all()
    }

    return render(request, 'exibicao/subarea.html', subareas)

def topico(request):

    topicos = {
        'topicos':Topico.objects.all()
    }

    return render(request, 'exibicao/topico.html', topicos)

def fisico(request):

    fisicos = {
        'fisicos':Fisico.objects.all()
    }

    return render(request, 'exibicao/fisico.html', fisicos)

def invencao(request):

    invencoes = {
        'invencoes':Invencao.objects.all()
    }

    return render(request, 'exibicao/invencao.html', invencoes)

def questionario(request):

    questionarios = {
        'questionarios':Questionario.objects.all(),
        'questoes':Questao.objects.all()
    }

    return render(request, 'exibicao/questionario.html', questionarios)

def ocupacao(request):

    ocupacoes = {
        'ocupacoes':Ocupacao.objects.all()
    }

    return render(request, 'exibicao/ocupacao.html', ocupacoes)

def pessoa(request):

    pessoas = {
        'pessoas':Pessoa.objects.all()
    }

    return render(request, 'exibicao/pessoa.html', pessoas)

def questionario(request):

    questionarios = {
        'questionarios':Questionario.objects.all()
    }

    return render(request, 'exibicao/questionario.html', questionarios)