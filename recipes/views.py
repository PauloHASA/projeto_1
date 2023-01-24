from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contato(request):
    return HttpResponse('CONTATO do App View')


def sobre(request):
    return HttpResponse('SOBRE do App View')
