from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)


from applications.home.models import Blog


# Create your views here.

"""class HomePageView(TemplateView):
    template_name = "home/index.html"""
    
class PoliticadeprivacidadView(TemplateView):
    template_name = "politica-de-privacidad.html"


class Politica_de_cookiesView(TemplateView):
    template_name = "politica-de-cookies.html"


class AvisolegalView(TemplateView):
    template_name = "aviso-legal.html"


class HomePageView(ListView):
    template_name = "home/index.html"
    model = Blog
    context_object_name = 'entradas_blog'
    def get_queryset(self):
        # Obtenemos el queryset original
        queryset = super().get_queryset()
        # Filtramos y seleccionamos el primer objeto
        first_item = queryset.first()
        # Si no hay objetos en el queryset, devolvemos un queryset vacío
        if first_item is None:
            return queryset.none()
        # Devolvemos un queryset que contiene solo el primer objeto
        return queryset.order_by('-id')[:3]

class BlogView(ListView):
    model = Blog
    template_name = 'home/Blog.html'
    context_object_name = 'entradas_blog'
    ordering = [
        '-fecha_hora'
    ]

class BlogDetailView(DetailView):
    model = Blog # Especifica el modelo Blog
    template_name = 'home/articulo_completo.html' # Define el template "articulo_completo.html"
    context_object_name = 'articulo'

