from django.urls import path
from .views import home,articoloDetailView, lista_articoli, lista__tutti_articoli

app_name = 'news'

urlpatterns = [
    path('', home, name='home'),
    path('articoli/<int:pk>/', articoloDetailView, name='articolo_detail'),
    path('lista_articoli/<int:pk>/', lista_articoli, name='lista_articoli_giornalista'),
    path('lista_articoli/', lista__tutti_articoli, name='lista_articoli')
]