from django.shortcuts import render
from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True).order_by('-datetime_modified')
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 4

    # def get_queryset(self):
    #     return Product.objects.filter(active=True).order_by('-datetime_modified')


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
