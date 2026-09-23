from django.urls import path
from . import views

app_name="prima_app"
urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('welcome/', views.welcome, name='welcome'),
    path('lista/', views.lista, name='lista'),
    path('chi_siamo/', views.chi_siamo, name='chi_siamo'),
    path('variabili/', views.variabili, name='variabili'),
]