from products.models import Product


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
            self.cart[product_id] = {'quantity': quantity}
        else:
            if override:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product, ):
        """
        Remove a product from cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
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
            cart[str(product.id)]['product_object'] = product

        for item in cart.values():
            yield item

    def __len__(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        products = self.get_product_objects()
        return sum(product.price for product in products)

    def get_product_objects(self):
        product_ids = self.cart.keys()
        return Product.objects.filter(id__in=product_ids)
