# FILE: LinksVercel/urls.py

from django.contrib import admin
from django.urls import path
from . import views  # Importar views do mesmo diretório

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]