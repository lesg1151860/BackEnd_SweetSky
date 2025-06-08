from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from sweetsky.models import Sauce, Topping, Product, Presentation, Order
from datetime import timedelta

class SauceModelTest(TestCase):
    def test_create_sauce(self):
        print("Ejecutando: test_create_sauce...", end=' ')
        try:
            sauce = Sauce.objects.create(name="Chocolate")
            self.assertEqual(sauce.name, "Chocolate")
            self.assertTrue(sauce.status)
            self.assertIsNotNone(sauce.creation_date)
            self.assertEqual(str(sauce), "Chocolate")
            print("OK")
        except Exception as e:
            print("FAILED")
            raise e

class ToppingModelTest(TestCase):
    def test_create_topping(self):
        print("Ejecutando: test_create_topping...", end=' ')
        try:
            topping = Topping.objects.create(name="Chispas")
            self.assertEqual(topping.name, "Chispas")
            self.assertTrue(topping.status)
            self.assertIsNotNone(topping.creation_date)
            self.assertEqual(str(topping), "Chispas")
            print("OK")
        except Exception as e:
            print("FAILED")
            raise e

class ProductModelTest(TestCase):
    def test_create_product(self):
        print("Ejecutando: test_create_product...", end=' ')
        try:
            product = Product.objects.create(name="Helado")
            self.assertEqual(product.name, "Helado")
            self.assertTrue(product.status)
            self.assertIsNotNone(product.creation_date)
            self.assertEqual(str(product), "Helado")
            print("OK")
        except Exception as e:
            print("FAILED")
            raise e

class PresentationModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Helado")

    def test_create_presentation(self):
        print("Ejecutando: test_create_presentation...", end=' ')
        try:
            presentation = Presentation.objects.create(
                name="Vaso pequeño",
                product=self.product,
                price=5000,
                description="Presentación pequeña",
                status=True
            )
            self.assertEqual(presentation.name, "Vaso pequeño")
            self.assertEqual(presentation.product, self.product)
            self.assertEqual(presentation.price, 5000)
            self.assertTrue(presentation.status)
            self.assertIsNotNone(presentation.creation_date)
            self.assertIn("Vaso pequeño", str(presentation))
            print("OK")
        except Exception as e:
            print("FAILED")
            raise e

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="cliente", password="12345")
        self.product = Product.objects.create(name="Helado")
        self.presentation = Presentation.objects.create(
            name="Vaso grande",
            product=self.product,
            price=10000,
            description="Grande",
            status=True
        )

    def test_create_order_valid(self):
        print("Ejecutando: test_create_order_valid...", end=' ')
        try:
            delivery_date = timezone.now().date() + timedelta(days=1)
            order = Order.objects.create(
                client=self.user,
                presentation=self.presentation,
                delivery_address="Calle 123",
                city="Cúcuta",
                delivery_date=delivery_date,
                delivery_time="15:00",
                delivery=True
            )
            self.assertEqual(order.client, self.user)
            self.assertEqual(order.presentation, self.presentation)
            self.assertEqual(order.city, "Cúcuta")
            self.assertEqual(order.status, "pendiente")
            self.assertIsNotNone(order.creation_date)
            self.assertEqual(order.total_price, self.presentation.price + 6000)
            self.assertIn("cliente", str(order))
            print("OK")
        except Exception as e:
            print("FAILED")
            raise e

    def test_order_total_price_without_delivery(self):
        print("Ejecutando: test_order_total_price_without_delivery...", end=' ')
        try:
            delivery_date = timezone.now().date() + timedelta(days=1)
            order = Order.objects.create(
                client=self.user,
                presentation=self.presentation,
                delivery_address="Calle 123",
                city="Cúcuta",
                delivery_date=delivery_date,
                delivery_time="15:00",
                delivery=False
            )
            self.assertEqual(order.total_price, self.presentation.price)
            print("OK")
        except Exception as e:
            print("FAILED")
            raise e

    def test_order_invalid_past_date(self):
        print("Ejecutando: test_order_invalid_past_date...", end=' ')
        delivery_date = timezone.now().date() - timedelta(days=1)
        try:
            with self.assertRaises(Exception):
                Order.objects.create(
                    client=self.user,
                    presentation=self.presentation,
                    delivery_address="Calle 123",
                    city="Cúcuta",
                    delivery_date=delivery_date,
                    delivery_time="15:00",
                    delivery=True
                )
            print("OK")
        except Exception as e:
            print("FAILED")
            raise e

    def test_order_invalid_city_for_delivery(self):
        print("Ejecutando: test_order_invalid_city_for_delivery...", end=' ')
        delivery_date = timezone.now().date() + timedelta(days=1)
        try:
            with self.assertRaises(Exception):
                Order.objects.create(
                    client=self.user,
                    presentation=self.presentation,
                    delivery_address="Calle 123",
                    city="Ciudad Falsa",
                    delivery_date=delivery_date,
                    delivery_time="15:00",
                    delivery=True
                )
            print("OK")
        except Exception as e:
            print("FAILED")
            raise e