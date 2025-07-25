from django.contrib import admin

from .models import administration, cart, product, Stuff

admin.site.register(administration)
admin.site.register(cart)
admin.site.register(product)
admin.site.register(Stuff)