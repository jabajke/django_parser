from django.urls import path
from store_app.views import *

urlpatterns = [
    path('', ShowItemView.as_view(), name='show_item'),
    path('index/', IndexView.as_view(), name='index'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('categories/<str:i>', CategoryItemView.as_view(), name='category_item'),
    path('product/', ProductView.as_view(), name='product'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_cart/<int:pk>', add_to_cart, name='add_cart'),
    path('cart/up_down/<str:pk>', OnClickView.as_view(), name='onclick'),
    path('cart/clear_cart', clear_cart, name='clear'),
    path('get_count/', GetCountView.as_view(), name='get_count')

]
