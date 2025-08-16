from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('main/', views.index, name="main"),
    path('contact_us/', views.contact_us, name="test_form"),
    path('about_me/', views.about_me, name="about me"),
    path('register/', views.register, name="register"),
    path('login/', views.login_p, name="login"),
    path('logout/', views.logout_request, name="logout"),
    path('create_stuff/', views.create_stuff, name='create stuff'),
    path('admin_page/', views.admin_top_main_staff, name='admin top main staff'),
    path('reset_password/', views.password_reset_request, name='reset_password'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete")
]