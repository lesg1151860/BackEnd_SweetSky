from django.contrib import admin
from django.contrib.auth.models import User

from .models import Sauce, Topping, Product, Presentation, Order

# Registrar modelos básicos
admin.site.register(Sauce)
admin.site.register(Topping)
admin.site.register(Product)
admin.site.register(Order)

# Si deseas personalizar el admin de User, descomenta lo siguiente:
# from django.contrib.auth.admin import UserAdmin
# admin.site.unregister(User)
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'is_staff', 'is_active')

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'price', 'status')
    list_filter = ('product', 'status')
    search_fields = ('name', 'product__name')
    list_editable = ('status',)
    ordering = ('-creation_date',)
