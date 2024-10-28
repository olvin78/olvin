from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)


# Create your views here.

class HomePageView(TemplateView):
    template_name = "index.html"
    
class PoliticadeprivacidadView(TemplateView):
    template_name = "politica-de-privacidad.html"


class Politica_de_cookiesView(TemplateView):
    template_name = "politica-de-cookies.html"


class AvisolegalView(TemplateView):
    template_name = "aviso-legal.html"
