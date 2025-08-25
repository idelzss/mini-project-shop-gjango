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
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
    path("cart/", views.view_cart, name="view_cart"),
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path("admin_panel/", views.admin_panel, name="admin_panel"),
    path('admin_panel/delete/<int:staff_id>/', views.delete_staff, name='delete_stuff'),
    path('admin_panel/redact/<int:stuff_id>/', views.redact_stuff, name='redact_stuff'),
]