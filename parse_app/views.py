from django.shortcuts import redirect

from bs4 import BeautifulSoup
import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ParseData


class GetLinkView(APIView):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/95.0.4638.69 Safari/537.36', 'accept': '*/*'}

    def post(self, request):
        link = request.data['link']
        html = self.get_html(link)
        return Response({'data': self.get_content(html.content)})

    def get_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('li', class_='result__item')
        goods_2 = []
        for item in items:
            goods = {'title': item.find('span', class_="result__name").get_text(),
                     'price': self.convert_to_float(item),
                     'image': item.find('span', class_="result__img").get_text(),
                     'category': self.valid_string(item),
                     }
            ParseData.objects.create(**goods)
            goods_2.append(goods)
        return goods_2

    def get_html(self, link, params=None):
        r = requests.get(link, params=params)
        return r

    def convert_to_float(self, item):
        p = item.find('span', class_="g-item-data").get_text()
        p_1 = p.replace(',', '.')
        price = float(p_1.replace(' ', ''))
        return price

    def valid_string(self, item):
        cat = item.find('h1', class_="content__header").get_text()
        cat_1 = cat.replace('(', '')
        cat_2 = cat_1.replace(')', '')
        cat_3 = cat_2.replace("'", "")
        category = cat_3.replace(",", '')
        return category

