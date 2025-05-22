from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, "test.html")

def test2(request):
    return render(request, "test2.html")

def test3(request):
    now = datetime.datetime.now()
    return HttpResponse(f"{now}")


def about(request):
    return render(request, "about.html")

def test_form(request):
    return render(request, "test_form.html")