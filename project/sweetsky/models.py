from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Sauce(models.Model):
    name = models.CharField(max_length=100, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=100, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Presentation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='presentations/', blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.price} COL$"


class Order(models.Model):
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_camino', 'En Camino'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    CITY_CHOICES = [
        ('Cúcuta', 'Cúcuta'),
        ('Los Patios', 'Los Patios'),
        ('Villa del Rosario', 'Villa del Rosario'),
    ]
    
    DELIVERY_PRICES = {
        'Cúcuta': 6000,
        'Los Patios': 8000,
        'Villa del Rosario': 8000,
    }

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    delivery_address = models.TextField(max_length=300)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    delivery = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')
    creation_date = models.DateTimeField(auto_now_add=True)

    def calcular_total_price(self):
        base_price = self.presentation.price
        delivery_price = self.DELIVERY_PRICES.get(self.city, 0) if self.delivery else 0
        return base_price + delivery_price

    def clean(self):
        if self.delivery_date < timezone.now().date():
            raise ValidationError("La fecha de entrega no puede ser en el pasado.")
        
        if self.delivery and self.city not in self.DELIVERY_PRICES:
            raise ValidationError("Ciudad no válida para servicio de domicilio")

    def save(self, *args, **kwargs):
        self.total_price = self.calcular_total_price()
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido #{self.id} - {self.client.username}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-creation_date']