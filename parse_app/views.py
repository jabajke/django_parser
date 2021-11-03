from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout, get_user_model

from bs4 import BeautifulSoup
import requests

from rest_framework.views import APIView
from rest_framework.response import Response



def index(request):
    pass


class LoginView(APIView):

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            login(request, user)
        if not request.user.is_authenticated:
            create = get_user_model().objects.create_user(**request.data)
            login(request, create)
        return redirect('index')


def do_logout(request):
    logout(request)
    return redirect('login')


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
        print(items)
        goods = []
        for item in items:
            try:
                goods.append({'title': item.get_text()})
            except Exception as e:
                print(e)
        print(goods)
        return goods

    def get_html(self, link, params=None):
        r = requests.get(link, params=params)
        return r
