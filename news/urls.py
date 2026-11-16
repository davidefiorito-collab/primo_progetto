from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name='index'),
    path('articoli/<int:pk>/', views.articoloDetailView, name='articolo_detail'),
    path('lista_articoli/<int:pk>/', views.listaArticoli, name='lista_articoli_giornalista'),
    path('lista_articoli/', views.listaTuttiArticoli, name='lista_articoli'),
    path('query_base/', views.queryBase, name='query_base'),
    path('giornalisti/<int:pk>/', views.giornalistaDetailView, name='giornalista_detail'),
]