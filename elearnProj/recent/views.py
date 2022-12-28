from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Страница приложения последних 10 вакансий</h1>")
