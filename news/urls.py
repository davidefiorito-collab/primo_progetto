from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.home, name='home'),
    path('articoli/<int:pk>/', views.articoloDetailView, name='articolo_detail'),
    path('lista_articoli/<int:pk>/', views.lista_articoli, name='lista_articoli_giornalista'),
    path('lista_articoli/', views.lista_tutti_articoli, name='lista_articoli'),
    path('query_base/', views.query_base, name='query_base')
]