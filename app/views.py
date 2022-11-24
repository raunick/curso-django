from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def home(response):
    return render(response, 'home.html')


def painel(response):
    return render(response, 'painel.html')


def contato(response):
    return render(response, 'contato.html')
