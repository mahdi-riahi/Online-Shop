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
