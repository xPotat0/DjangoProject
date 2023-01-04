from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'demand/index.html')

def geography(request):
    return render(request, 'demand/geography.html')
