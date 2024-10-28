from os import name
from django.urls import include, path
from . import views


"""
{% url 'home_app:aviso_legal' %}
{% url 'home_app:politica_de_privacidad' %}
{% url 'home_app:politica_de_cookies' %}
"""

app_name = 'home_app'

urlpatterns = [
    path('',
        views.HomePageView.as_view(),
        name='home',
    ),

    path('Politica de privacidad',
        views.PoliticadeprivacidadView.as_view(),
        name='politica-de-privacidad',
    ),


     path('Aviso legal',
        views.AvisolegalView.as_view(),
        name='aviso_legal',
    ),


    path('Politica de cookies',
        views.Politica_de_cookiesView.as_view(),
        name='politica-de-cookies',
    ),


]