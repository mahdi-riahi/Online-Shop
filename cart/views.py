from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from .forms import AddToCartForm

from products.models import Product


def cart_detail_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', context={'cart': cart})


def add_to_cart_view(request, product_id):
    product = get_object_or_404(Product, id=int(product_id))
    cart = Cart(request)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity)
        return redirect('cart:cart_detail')


# class CartDetailView(generic.TemplateView):
#     template_name = 'cart/cart_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cart'] = Cart(self.request)
#         return context
