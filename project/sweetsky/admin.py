from django.contrib import admin
from .models import Sauce, Topping, Product, Presentation, Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'presentation', 'total_price', 'status', 'creation_date')
    list_filter = ('status', 'city', 'delivery')
    search_fields = ('client__username', 'delivery_address')
    date_hierarchy = 'creation_date'
    readonly_fields = ('total_price', 'creation_date')

admin.site.register(Sauce)
admin.site.register(Topping)
admin.site.register(Product)
admin.site.register(Presentation)