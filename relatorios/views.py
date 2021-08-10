from django.shortcuts import render
from django.views.generic import TemplateView
from KolbStyleTeste.models import Resposta

# Create your views here.


def relatorio(request):

    return render(request, "relatorio.html", context={})
