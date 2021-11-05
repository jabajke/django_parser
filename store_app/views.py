from rest_framework.views import APIView
from rest_framework.response import Response

from parse_app.models import ParseData


class ShowItemView(APIView):

    def post(self, request):
        category = request.data['category']
        goods = ParseData.objects.filter(category=category)
        return Response(goods)

