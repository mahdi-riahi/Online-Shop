from django.db import models
from django.urls import reverse


class Product(models.Model):
    # CATEGORIES = (
    #     ('BK', 'Books'),
    #     ('SM', 'Smart Phones'),
    #     ('ED', 'Electronic Devices'),
    # )
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    # category = models.CharField(choices=CATEGORIES, null=False, blank=True, max_length=2)
    # cover = models.ImageField(upload_to=)
    # storage = models.PositiveIntegerField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk, ])


class Comment(models.Model):
    STARS = (
        (1, 'بی کیفیت'),
        (2, 'بد'),
        (3, 'متوسط'),
        (4, 'خوب'),
        (5, 'عالی'),
    )
    RECOMMENDATIONS = (
        (True, 'این محصول را پیشنهاد می کنم'),
        (False, 'این محصول را پیشنهاد نمی کنم'),
    )
    text = models.TextField(verbose_name='متن نظر شما')
    author = models.CharField(max_length=100, verbose_name='نام')
    author_email = models.EmailField(blank=False, verbose_name='ایمیل')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    stars = models.PositiveIntegerField(choices=STARS, blank=False, verbose_name='امتیاز')
    recommendation = models.BooleanField(default=True, choices=RECOMMENDATIONS, verbose_name='پیشنهاد به دیگران')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.product.pk, })
