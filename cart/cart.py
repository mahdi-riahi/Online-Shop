from products.models import Product
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class Cart:
    def __init__(self, request):
        """
        Initialize the Cart
        """
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity=1, override=False):
        """
        Add product to the cart if existed
        if replace equals 'True' the amount of given quantity will be replaced instead of self.cart[product_id]['quantity']
        if replace equals 'False' as it is on default, the amount of given quantity will be added to self.cart[product_id]['quantity']
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if override:
            self.cart[product_id]['quantity'] = quantity
            messages.success(self.request, _('Product quantity updated'))
        else:
            self.cart[product_id]['quantity'] += quantity
            messages.success(self.request, _('Product added to cart successfully'))

        self.save()

    def reduce(self, product, quantity=1):
        """
        Decrease and reduce from cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] -= quantity
            if self.cart[product_id]['quantity'] == 0:
                del self.cart[product_id]
            self.save()

    def remove(self, product, ):
        """
        Remove a product from cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            messages.info(self.request, _('Product removed from cart'))
            self.save()

    def save(self):
        """
        Mark session as modified to save changes
        """
        self.session.modified = True

    def __iter__(self):
        products = self.get_product_objects()
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['object'] = product
            cart[str(product.id)]['item_price'] = cart[str(product.id)]['quantity'] * product.price

        for item in cart.values():
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Clean the cart completely
        """
        del self.session['cart']
        self.save()

    def get_total_price(self):
        """
        Calculate total price of the cart items
        """
        # products = self.get_product_objects()
        # total = [self.get_item_price(product) for product in products]
        # return sum(total)
        return sum(item['quantity'] * item['object'].price for item in self.cart.values())

    def get_product_objects(self):
        """
        Get all objects in the cart
        """
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)

    def get_item_price(self, product):
        """
        Calculate each item's cost in the cart
        """
        quantity = self.cart[str(product.id)]['quantity']
        price = product.price
        return quantity * price
