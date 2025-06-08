from django.urls import path
from . import views

app_name = 'sweetsky'

urlpatterns = [
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/update/', views.OrderUpdateView.as_view(), name='order-update'),
    path('presentations/', views.PresentationListView.as_view(), name='presentation-list'),
    path('presentations/create/', views.PresentationCreateView.as_view(), name='presentation-create'),
    path('presentations/<int:pk>/', views.PresentationDetailView.as_view(), name='presentation-detail'),
    path('presentations/<int:pk>/update/', views.PresentationUpdateView.as_view(), name='presentation-update'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),
    path('toppings/', views.ToppingListView.as_view(), name='topping-list'),
    path('toppings/create/', views.ToppingCreateView.as_view(), name='topping-create'),
    path('toppings/<int:pk>/', views.ToppingDetailView.as_view(), name='topping-detail'),
    path('toppings/<int:pk>/update/', views.ToppingUpdateView.as_view(), name='topping-update'),
    path('sauces/', views.SauceListView.as_view(), name='sauce-list'),
    path('sauces/create/', views.SauceCreateView.as_view(), name='sauce-create'),
    path('sauces/<int:pk>/', views.SauceDetailView.as_view(), name='sauce-detail'),
    path('sauces/<int:pk>/update/', views.SauceUpdateView.as_view(), name='sauce-update'),
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    
]