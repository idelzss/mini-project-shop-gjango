from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm, LoginForm, AdminForm
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

def about_me(request):
    return render(request, "about_me.html")





def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("index")
    form = NewUserForm()
    return render(request=request,
                  template_name="register.html",
                  context={"register_form": form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect("index")
    form = LoginForm()
    return render(request=request,
                  template_name="login.html",
                  context={"login_form": form})

def admin(request):
    form = AdminForm()
    return render(request=request,
                  template_name="admin_form.html",
                  context={"admin_form": form})