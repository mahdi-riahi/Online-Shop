from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home_page.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='pages/about_page.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='pages/contact_page.html'), name='contact'),
]
