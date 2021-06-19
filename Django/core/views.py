from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm
# Create your views here.
def registro (request):
    return render(request, 'core/Registro.html')
    