from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


class SobreView(TemplateView):
    template_name = 'sobre.html'


class QuemSomosView(TemplateView):
    template_name = 'quem-somos.html'


class ComoFuncionaView(TemplateView):
    template_name = 'como-funciona.html'
