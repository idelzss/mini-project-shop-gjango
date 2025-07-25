from django.urls import path

from . import views

urlpatterns = [
    path('main/', views.index, name="main"),
    path('about/', views.about, name="about"),
    path('test/', views.test, name="test"),
    path('test2/', views.test2, name="test2"),
    path('test_form/', views.test_form, name="test_form"),
    path('test3/', views.test3, name="test3"),
    path('about_me/', views.about_me, name="about me"),
    path('register/', views.register, name="register"),
    path('login/', views.login_p, name="login"),
    path('admin_form/', views.admin, name="admin"),
    path('logout/', views.logout_request, name="logout"),
    path('create_stuff', views.create_stuff, name='create stuff')
]