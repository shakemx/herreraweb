from django.shortcuts import render, redirect

from seguro.models import  Seguro
from modalidad.models import Modalidad

def home(request):
    if request.method == 'GET':
        seguros = Modalidad.objects.filter(is_active=True)
        context = {'seguros': seguros}
        return render(request, 'home.html', context)
    return redirect('home')