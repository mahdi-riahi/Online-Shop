from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import OrderForm
from .models import OrderItem,Order
from cart.cart import Cart


@login_required
def order_create_view(request):
    cart = Cart(request)
    form = OrderForm(request.POST or None)
    if form.is_valid() and cart:
        order = form.save(commit=False)
        order.user = request.user
        order.save()

        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['object'],
                price=item['object'].price,
                quantity=item['quantity'],
            )
        cart.clear()

        messages.success(request, _('Your Order has been registered'))
        return redirect('order:order_detail', pk=order.id)

    if request.user.orders:
        order = request.user.orders.last()
        form = OrderForm(initial={
            'first_name': order.first_name,
            'last_name': order.last_name,
            'phone_number': order.phone_number,
            'address': order.address,
        })

    return render(request, 'orders/order_create.html', {'form': form})


class OrderListView(LoginRequiredMixin, generic.ListView):
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-datetime_modified')


class OrderDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Order
    template_name = 'orders/order_detail.html'

    def test_func(self):
        return self.request.user == self.get_object().user
