from django.urls import path
from store_app.views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', ShowItemView.as_view(), name='show_item'),
    path('index/', IndexView.as_view(), name='index'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/<str:i>', TemplateView.as_view(template_name='store_app/categories.html'), name='category_item'),
    path('product/', ProductView.as_view(), name='product'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('cart/', CartView.as_view(), name='cart'),

]
