from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import NewUserForm, LoginForm, AdminForm, StuffForm
import datetime

from .models import Stuff


def index(request):
    all_staff = Stuff.objects.all()
    return render(request, 'index.html', {"staff" : all_staff})


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
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request,
                  template_name="register.html",
                  context={"register_form": form} )

def login_p(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main")
            else:
                messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"login_form": form} )


def admin(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
        else:
            print(form.errors)
    else:
        form = AdminForm()

    return render(request, "admin_form.html", {"admin_form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request=request,
                  template_name="logout.html",
                  )



def test_page(request):
    stuff = Stuff.objects.all()
    paginator = Paginator(stuff, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'test.html', context={"page_obj": page_obj})


def create_stuff(request):
    if request.method == "POST":
        form = StuffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main")
        else:
            print(form.errors)
    else:
        form = StuffForm()

    return render(request, "stuff_form.html", {"stuff_form": form})