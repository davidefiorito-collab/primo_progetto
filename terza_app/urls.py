from django.urls import path
from . import views

app_name="terza_app"
urlpatterns=[
    path('', views.index, name='index'),
    path('view_a/', views.view_a, name='view_a'),
    path('view_b/', views.view_b, name='view_b'),
    path('view_c/', views.view_c, name='view_c'),
]