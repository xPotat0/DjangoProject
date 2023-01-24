from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from elearnProj.hh_api import main_


def index(request):
    index_ = Index.objects.all()
    return render(request, 'demand/index.html', {'index': index_})


def geography(request):
    geography = Geography.objects.all()
    return render(request, 'demand/geography.html', {'geography': geography, 'name': [('Город', 'Зарплата', '5', 'sal'), ('Город', 'Кол-во', '6', 'amo')]})


def demand(request):
    demand = Demand.objects.all()
    return render(request, 'demand/demand.html', {'demand': demand, 'name': [('Год', 'Кол-во', '1', 'va'), ('Год', 'Зарплата', '2', 'sl'), ('Год', 'Кол-во', '3', 'vad'), ('Год', 'Зарплата', '4', 'sld')]})


def skills(request):
    skill = Skills.objects.all()
    return render(request, 'demand/skills.html', {'skill': skill, 'year': [("2015", 'div111'), ("2016", 'div222'), ("2017", 'div333'), ("2018", 'div444'), ("2019", 'div555'), ("2020", 'div666'), ("2021", 'div777'), ("2022", 'div888')]})


def last(request):
    table = main_()
    return render(request, 'demand/last.html', {'table': table})