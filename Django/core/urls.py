from django.urls import path
from .views import delete_cliente, registro, registrados, add_cliente, edit_cliente

urlpatterns = [
    path('', registro, name= "registro"),
    path('registrados/', registrados, name= "registrados"),
    path('add_cliente/', add_cliente, name="add_cliente"),
    path('edit_cliente/<pk>/', edit_cliente, name="edit_cliente"),
    path('delete_cliente/<pk>/', delete_cliente, name="delete_cliente"),
]