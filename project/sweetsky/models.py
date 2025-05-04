from django.db import models
from django.contrib.auth.models import User


# Modelo para Salsas
class Sauce(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nombre de la salsa
    date_creacion = models.DateTimeField(auto_now_add=True)  # Fecha y hora automática al crear
    status = models.BooleanField(default=True)  # Estado: Activo (True) o Inactivo (False)

    def __str__(self):
        return self.name


# Modelo para Toppings
class Topping(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nombre del topping
    date_creacion = models.DateTimeField(auto_now_add=True)  # Fecha y hora automática al crear
    status = models.BooleanField(default=True)  # Estado: Activo (True) o Inactivo (False)

    def __str__(self):
        return self.name


# Modelo para Producto
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Nombre del producto
    date_creacion = models.DateTimeField(auto_now_add=True)  # Fecha y hora automática al crear
    status = models.BooleanField(default=True)  # Estado: Activo (True) o Inactivo (False)

    def __str__(self):
        return self.name
    

# Modelo para Presentación
class Presentation(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the presentation
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # Relation with Product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    creation_date = models.DateTimeField(auto_now_add=True)  # Date and time of creation
    description = models.TextField(max_length=500, blank=True, null=True)  # Short description
    image = models.URLField(max_length=500, blank=True, null=True)  # URL for the image
    status = models.BooleanField(default=True)  # Status: Active (True) or Inactive (False)

    def __str__(self):
        return f"{self.name} - {self.price} COL$"  # Returns the name and price of the presentation
    

# Modelo para Orden de Pedido
class Order(models.Model):
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_camino', 'En Camino'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    CITY_CHOICES = [
        ('Cúcuta', 6000),
        ('Los Patios', 8000),
        ('Villa del Rosario', 8000),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario (cliente)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)  # Relación con Presentación
    delivery_address = models.TextField(max_length=300)  # Dirección de entrega
    city = models.CharField(max_length=50, choices=[(city, city) for city, _ in CITY_CHOICES])  # Ciudad
    delivery_date = models.DateField()  # Fecha de entrega
    delivery_time = models.TimeField()  # Hora de entrega
    delivery = models.BooleanField(default=False)  # Si requiere domicilio
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Precio total
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')  # Estado del pedido
    date_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación del pedido

    def calcular_total_price(self):
        price_presentation = self.presentation.price
        price_delivery = next((price for city, price in self.CITY_CHOICES if city == self.city), 0) if self.delivery else 0
        return price_presentation + price_delivery

    def save(self, *args, **kwargs):
        self.total_price = self.calcular_total_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido de {self.client.get_full_name()} - {self.presentation.name}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-date_creacion']
