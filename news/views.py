from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello World")


def test(request):
    return HttpResponse("<h1>Тестовая страница с разметкой</h1>")
