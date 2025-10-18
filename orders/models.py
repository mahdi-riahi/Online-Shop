from datetime import date, timedelta

from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    ORDER_STATUSES = (
        ('np', _('Not Paid')),
        ('pr', _('Preparing')),
        ('se', _('Sent')),
        ('de', _('Delivered')),
        ('ca', _('Canceled')),
        ('rt', _('Returned')),
    )
    RECEIVE_DATES = (
        (date.today() + timedelta(days=4), date.today() + timedelta(days=4)),
        (date.today() + timedelta(days=5), date.today() + timedelta(days=5)),
        (date.today() + timedelta(days=6), date.today() + timedelta(days=6)),
        (date.today() + timedelta(days=7), date.today() + timedelta(days=7)),
    )
    user = models.ForeignKey(verbose_name=_('User'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='orders')
    is_paid = models.BooleanField(default=False)
    status = models.CharField(_('Order Status'), choices=ORDER_STATUSES, max_length=2, default=ORDER_STATUSES[0][0])

    phone_number = models.CharField(_('Phone Number(IR)'), max_length=11, null=False, )
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    address = models.CharField(_('Full Address'), max_length=700)
    # email = models.EmailField(_('Email')) # We can add email if we didn't use email verification for login
    note = models.TextField(_('Extra Note'), blank=True)

    datetime_created = models.DateTimeField(_('Order Added At'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('Order Updated At'), auto_now=True)

    date_receive = models.DateField(_('Choose Receive Date'), choices=RECEIVE_DATES, default=RECEIVE_DATES[0][0])

    def __str__(self):
        return f'Order {self.id} for {self.user}'

    def get_absolute_url(self):
        return reverse('order:order_detail', args=[self.id])

    def get_total_price(self):
        return sum(item.price * item.quantity for item in self.items.all())

    def __len__(self):
        return sum(item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(verbose_name=_('Order'), to=Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(
        verbose_name=_('Product'), to='products.Product', on_delete=models.CASCADE, related_name='order_items'
    )
    price = models.PositiveIntegerField(_('Price'))
    quantity = models.PositiveIntegerField(_('Quantity'), default=1)

    # We can use order to get datetimes
    # datetime_created = models.DateTimeField(_('Item Added At'), auto_now_add=True)
    # datetime_modified = models.DateTimeField(_('Item Updated At'), auto_now=True)

    def __str__(self):
        return f'Order Item {self.id} for order {self.order.id}: {self.quantity} x {self.product.title[:20]} ({self.price})'
