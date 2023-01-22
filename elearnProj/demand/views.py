from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'demand/index.html')


def geography(request):
    return render(request, 'demand/geography.html')


def demand(request):
    return render(request, 'demand/demand.html')


def skills(request):
    return render(request, 'demand/skills.html')


def last(request):
    return render(request, 'demand/last.html')