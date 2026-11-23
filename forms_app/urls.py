from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('contattaci/', views.contatti, name='contatti'),
]