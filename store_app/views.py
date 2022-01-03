from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

from parse_app.models import ParseData

from django.core.serializers import serialize

from store_app.cart import Cart


class ShowItemView(APIView):

    def post(self, request):
        category = list(ParseData.objects.filter(category=request.data['category']))
        category_serialize = serialize('json', category)
        return Response(category_serialize)


class IndexView(TemplateView):
    template_name = 'store_app/index.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        category = ParseData.objects.distinct().values('category')
        list_category = []
        for i in category:
            list_category.append(i['category'])
            self.extra_context['list_category'] = list_category
        return super().get(self, request, *args, **kwargs)


class CategoryView(IndexView):
    template_name = 'store_app/categories.html'


class ProductView(IndexView):
    template_name = 'store_app/product.html'


class ContactView(IndexView):
    template_name = 'store_app/contact.html'


class CartView(IndexView):
    template_name = 'store_app/cart.html'
    obj = ParseData.objects
    z = []

    def get(self, request):
        self.cart = Cart(request)
        for k in self.cart.cart:
            self.z.append({'id': k,
                           'image': self.obj.get(pk=k).image,
                           'qnty': self.cart.cart[k]['quantity'],
                           'price': self.cart.cart[k]['price'],
                           'total': self.cart.cart[k]['quantity'] * self.cart.cart[k]['price'],
                           'title': self.obj.get(pk=k).title
                           })
        self.extra_context['z'] = self.z
        return super().get(self, request)


def add_to_cart(request, pk):
    Cart(request).add(ParseData.objects.get(pk=pk))
    return redirect(reverse_lazy('categories'))


def clear_cart(request):
    Cart(request).clear()
    return redirect(reverse_lazy('index'))


class CheckoutView(IndexView):
    template_name = 'store_app/checkout.html'


class CategoryItemView(CategoryView):

    def get(self, request, i, **kwargs):
        self.extra_context['data'] = ParseData.objects.filter(category=i)
        self.extra_context['list_category_2'] = i
        return super().get(self, request, i)


class OnClickView(APIView):

    def post(self, request, pk):
        cart = Cart(request)
        if request.data['up']:
            cart.cart[pk]['quantity'] += 1
        if cart.cart[pk]['quantity'] > 1:
            if not request.data['up']:
                cart.cart[pk]['quantity'] -= 1
        cart.save()
        return Response([cart.cart[pk]['quantity'], cart.cart[pk]['quantity'] * cart.cart[pk]['price']])


class GetCountView(IndexView):

    def get(self, request):
        self.extra_context['count'] = len(request.session.get('cart'))
        return super().get(self, request)
