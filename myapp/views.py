from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, BadHeaderError
from django.contrib import messages
from django.core.paginator import Paginator
from django.template.loader import render_to_string

from .forms import NewUserForm, LoginForm, AdminForm, StuffForm
import datetime

from .models import Stuff


def index(request):
    staff = Stuff.objects.all()
    paginator = Paginator(staff, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = {
        "staff": staff,
        "stars":   range(1, 11),
        "page_obj": page_obj,
    }


    return render(request, 'index.html', context=context)


def test(request):
    return render(request, "test.html")

def test2(request):
    return render(request, "test2.html")

def test3(request):
    now = datetime.datetime.now()
    return HttpResponse(f"{now}")


def about(request):
    return render(request, "about.html")

def contact_us(request):
    return render(request, "contact_us.html")

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
    username = "not logged in"
    auth_form = AuthenticationForm(request.POST)
    if request.method == "POST":


        if auth_form.is_valid():
            username = auth_form.cleaned_data.get("username")
            password = auth_form.cleaned_data.get("password")
            authenticate(username=username, password=password)


    auth_form = AuthenticationForm()
    response = render(request, 'login', context={"auth_form": auth_form})
    response.set_cookie('username', username)
    response.set_cookie('last_connection', datetime.now())
    return response


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



def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': 'yourdomain.com',
                        'site_name': 'Your Site Name',
                        "uid": user.pk,
                        "user": user,
                        'token': user.auth_token.key,
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, "admin@gmail.com", [user.email], fail_silently=True)
                    except BadHeaderError:
                        messages.error(request, "Invalid header found.")
    password_reset_form = PasswordResetForm()
    return render(request,
                  "password_reset.html",
                  {"password_reset_form": password_reset_form})
