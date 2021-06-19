from django.urls import path
from .views import registro

urlpatterns = [
    path('', registro, name= "registro"),
]