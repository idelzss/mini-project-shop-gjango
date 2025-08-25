from django.contrib import admin
from .models import Stuff, Cart, CartItem

admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Stuff)



from django.contrib import admin


# @admin.register(Stuff)
# class MyModelAdmin(admin.ModelAdmin):
#     list_display = ('name', 'author')
#     list_filter = ('author',)
#     search_fields = ('name', 'author')
#     list_editable = ('name')
#
#     fieldsets = (
#         (
#             "Main", {
#                 'fields': ('name', 'author')
#             }
#         ),
#         (
#             "Secondary", {
#                 "fields": ('number',)
#             }
#         )
#     )
#
