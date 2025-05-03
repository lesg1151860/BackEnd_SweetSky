from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Presentation, Product, Sauce, Topping

admin.site.register(Sauce)
admin.site.register(Topping)
admin.site.register(Product)
admin.site.register(CustomUser, UserAdmin)

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'price', 'status')  # Campos visibles en la lista
    list_filter = ('product', 'status')  # Filtros por producto y estado
    search_fields = ('name', 'product__name')  # Búsqueda por nombre o producto
    list_editable = ('status',)  # Permite cambiar el estado con un solo clic
    ordering = ('-creation_date',)  # Ordena por fecha de creación, descendente
    