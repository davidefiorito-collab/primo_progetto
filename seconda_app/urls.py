from django.urls import path
from . import views

app_name = "seconda_app"

urlpatterns = [
    path("es_if/", views.es_if, name="es_if"),
    path("if_else_elif/", views.if_else_elif, name="if_else_elif"),
]