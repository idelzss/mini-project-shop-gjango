from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, "test.html")

def test2(request):
    return render(request, "test2.html")

def about(request):
    return render(request, "about.html")