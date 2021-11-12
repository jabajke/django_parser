from django.urls import path
from store_app.views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', ShowItemView.as_view(), name='show_item'),
    path('index/', IndexView.as_view(), name='index'),
    path('categories/', TemplateView.as_view(template_name='store_app/categories.html'), name='categories'),
    path('product/', TemplateView.as_view(template_name='store_app/product.html'), name='product'),
    path('checkout/', TemplateView.as_view(template_name='store_app/checkout.html'), name='checkout'),
    path('contact/', TemplateView.as_view(template_name='store_app/contact.html'), name='contact'),
    path('cart/', TemplateView.as_view(template_name='store_app/cart.html'), name='cart'),

]
