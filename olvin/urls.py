
#aca estoy inportando cada libreria con la que quiero trabajar
from django.contrib import admin
from django.urls import path,include



"""aca estoy indicando sobre lo que aprece en el navegador si en el navegador 
hay una url llevar al sitio web de la url, y si no hay nada entonces llevar al applications 
home o es decir llevar a la página principal"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.home.urls')),
]

