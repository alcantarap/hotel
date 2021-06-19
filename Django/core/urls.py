from django.urls import path
from .views import add_Cliente, registro, registrados

urlpatterns = [
    path('', registro, name= "registro"),
    path('registrados/', registrados, name= "registrados"),
    path('add_cliente/', add_Cliente, name="add_cliente")
]