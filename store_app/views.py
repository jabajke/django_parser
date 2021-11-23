from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

from parse_app.models import ParseData

from django.core.serializers import serialize
from django.shortcuts import render

from .models import CartModel, CartItem


class ShowItemView(APIView):

    def post(self, request):
        category = list(ParseData.objects.filter(category=request.data['category']))
        category_serialize = serialize('json', category)
        return Response(category_serialize)


class IndexView(TemplateView):
    template_name = 'store_app/index.html'
    category = ParseData.objects.distinct().values('category')
    list_category = []
    for i in category:
        list_category.append(i['category'])
        extra_context = {'list_category': list_category}


class CategoryView(IndexView):
    template_name = 'store_app/categories.html'


class ProductView(IndexView):
    template_name = 'store_app/product.html'


class ContactView(IndexView):
    template_name = 'store_app/contact.html'


class CartView(IndexView):
    template_name = 'store_app/cart.html'


class CheckoutView(IndexView):
    template_name = 'store_app/checkout.html'


class CategoryItemView(CategoryView):

    def get(self, request, i):
        self.extra_context['data'] = ParseData.objects.filter(category=i)
        self.extra_context['list_category_2'] = i
        return super().get(self, request, i)


class Cart:
    def add_to_cart(self, request, pk):
        goods = ParseData.objects.get(pk=pk)
        new_goods = CartModel.objects.get_or_create(goods=goods)
        cart = CartItem.objects.first()
        CartItem.items.create(new_goods)





