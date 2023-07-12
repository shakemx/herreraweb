from django.shortcuts import render, redirect


from modalidad.models import Modalidad

def home(request):
    if request.method == 'GET':
        seguros = Modalidad.objects.filter(is_active=True)
        context = {'seguros': seguros}
        return render(request, 'home/home.html', context=context) 
    return redirect('home')