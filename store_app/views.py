from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

from parse_app.models import ParseData

from django.core.serializers import serialize
from django.shortcuts import render


class ShowItemView(APIView):

    def post(self, request):
        category = list(ParseData.objects.filter(category=request.data['category']))
        category_serialize = serialize('json', category)
        return Response({'data': category_serialize})


class IndexView(TemplateView):
    template_name = 'store_app/index.html'
    extra_context = {'data': ParseData.objects.distinct().values('category')}
