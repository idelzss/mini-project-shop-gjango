from datetime import datetime

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, BadHeaderError
from django.contrib import messages
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .forms import NewUserForm, StuffForm


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
                  context={"register_form": form})


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

                response = redirect("main")
                response.set_cookie("username", username)
                response.set_cookie("last_connection", datetime.now())

                return response
            else:
                messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})




def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request=request,
                  template_name="logout.html",
                  )



def create_stuff(request):
        if not request.user.is_staff:
            return redirect("main")

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
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Idelzss market',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, "carshering.py@gmail.com", [user.email], fail_silently=True)
                    except BadHeaderError:
                        messages.error(request, "Invalid header found.")
    password_reset_form = PasswordResetForm()
    return render(request,
                  "password_reset.html",
                  {"password_reset_form": password_reset_form})



def admin_top_main_staff(request):
    if not request.user.is_staff:
        return redirect("main")
    else:
        staff = Stuff.objects.all()
        return render(request, "admin_top_main_staff.html", context={"staffs": staff})


