from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .cart import Cart
from .forms import AddToCartForm

from products.models import Product


def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = AddToCartForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })

    return render(request, 'cart/cart_detail.html', context={'cart': cart})


@require_POST
def add_to_cart_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        override = bool(cleaned_data['inplace'])
        cart.add(product, quantity, override)
        return redirect('cart:cart_detail')


@require_POST
def remove_from_cart_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart:cart_detail')


# class CartDetailView(generic.TemplateView):
#     template_name = 'cart/cart_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cart'] = Cart(self.request)
#         return context
