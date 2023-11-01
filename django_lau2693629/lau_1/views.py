from django.http import HttpResponse
from django.shortcuts import render
#def home(request):
#    return HttpResponse('<h1> hola mundo')

def home(request):
    return render(request, 'index.html')