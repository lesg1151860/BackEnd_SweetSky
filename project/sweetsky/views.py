from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Sauce, Topping, Presentation

class AdminRequiredMixin(UserPassesTestMixin):
    """
    Mixin para restringir el acceso solo a usuarios con rol de Administrador.
    Ajusta la condición según tu modelo de usuario.
    """
    def test_func(self):
        # Si usas un campo personalizado para el rol:
        # return self.request.user.is_authenticated and self.request.user.rol == 'Administrador'
        # Si usas el campo is_staff para administradores:
        return self.request.user.is_authenticated and self.request.user.is_staff

class SauceListView(ListView):
    model = Sauce
    template_name = 'sauces/sauce_list.html'
    context_object_name = 'sauces'

class SauceDetailView(DetailView):
    model = Sauce
    template_name = 'sauces/sauce_detail.html'
    context_object_name = 'sauce'

class SauceCreateView(AdminRequiredMixin, CreateView):
    model = Sauce
    fields = '__all__'
    template_name = 'sauces/sauce_form.html'
    success_url = '/sauces/'

class SauceUpdateView(AdminRequiredMixin, CreateView):
    model = Sauce
    fields = '__all__'
    template_name = 'sauces/sauce_form.html'
    success_url = '/sauces/'

class ToppingListView(ListView):
    model = Topping
    template_name = 'toppings/topping_list.html'
    context_object_name = 'toppings'

class ToppingDetailView(DetailView):
    model = Topping
    template_name = 'toppings/topping_detail.html'
    context_object_name = 'topping'

class ToppingCreateView(AdminRequiredMixin, CreateView):
    model = Topping
    fields = '__all__'
    template_name = 'toppings/topping_form.html'
    success_url = '/toppings/'
    
class ToppingUpdateView(AdminRequiredMixin, CreateView):
    model = Topping
    fields = '__all__'
    template_name = 'toppings/topping_form.html'
    success_url = '/toppings/'

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(AdminRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products/product_form.html'
    success_url = '/products/'

class ProductUpdateView(AdminRequiredMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products/product_form.html'
    success_url = '/products/'

class PresentationListView(ListView):
    model = Presentation
    template_name = 'presentations/presentation_list.html'
    context_object_name = 'presentations'

class PresentationDetailView(DetailView):
    model = Presentation
    template_name = 'presentations/presentation_detail.html'
    context_object_name = 'presentation'
    
class PresentationCreateView(AdminRequiredMixin, CreateView):
    model = Presentation
    fields = '__all__'
    template_name = 'presentations/presentation_form.html'
    success_url = '/presentations/'

def active_presentations(request):
    presentations = Presentation.objects.filter(status=True)
    return render(request, 'sweetsky/active_presentations.html', {'presentations': presentations})

class PresentationUpdateView(AdminRequiredMixin, CreateView):
    model = Presentation
    fields = '__all__'
    template_name = 'presentations/presentation_form.html'
    success_url = '/presentations/'

class OrderListView(ListView):
    model = Presentation
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'
    
class OrderDetailView(DetailView):
    model = Presentation
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(AdminRequiredMixin, CreateView):
    model = Presentation
    fields = '__all__'
    template_name = 'orders/order_form.html'
    success_url = '/orders/'

class OrderUpdateView(AdminRequiredMixin, CreateView):
    model = Presentation
    fields = '__all__'
    template_name = 'orders/order_form.html'
    success_url = '/orders/'

class HomeView(ListView):
    template_name = 'sweetsky/home.html'
    context_object_name = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_presentations'] = Presentation.objects.filter(status=True)
        return context

class AboutView(ListView):
    template_name = 'sweetsky/about.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_presentations'] = Presentation.objects.filter(status=True)
        return context

class ContactView(ListView):
    template_name = 'sweetsky/contact.html'
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_presentations'] = Presentation.objects.filter(status=True)
        return context
    def error_404_view(request, exception):
        return render(request, 'sweetsky/404.html', status=404)



