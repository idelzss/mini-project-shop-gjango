from django.urls import path

from . import views

urlpatterns = [
    path('main/', views.index, name="main"),
    path('about/', views.about, name="about"),
    path('test/', views.test, name="test"),
    path('test2/', views.test2, name="test2"),
]