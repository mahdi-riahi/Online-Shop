from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


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


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    STARS = (
        (1, _('Very Bad')),
        (2, _('Bad')),
        (3, _('Average')),
        (4, _('Good')),
        (5, _('Perfect')),
    )
    RECOMMENDATIONS = (
        (True, _('I recommend this product')),
        (False, _('I do not recommend this product')),
    )
    text = models.TextField(verbose_name=_('Your comment text'))
    author = models.CharField(max_length=100, verbose_name=_('Your name'))
    author_email = models.EmailField(blank=False, verbose_name=_('Email'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    stars = models.PositiveIntegerField(choices=STARS, blank=False, verbose_name=_('Score'))
    recommendation = models.BooleanField(
        default=True,
        choices=RECOMMENDATIONS,
        verbose_name=_('Do you suggest it to the others?'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # manager
    objects = models.Manager()
    active_comment_manager = ActiveCommentManager()

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.product.pk, })
