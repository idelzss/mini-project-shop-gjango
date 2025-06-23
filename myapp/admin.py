from django.contrib import admin

from .models import administration, cart, product

admin.site.register(administration)
admin.site.register(cart)
admin.site.register(product)