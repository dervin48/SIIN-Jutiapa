from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def myfirstview (request):
    data = {

        'entrada':entrada.objects.all()
    }

    return render(request, 'home.html', data)
