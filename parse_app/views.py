from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, get_user_model

from bs4 import BeautifulSoup
import requests

from rest_framework.views import APIView


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
        html = GetLinkView.get_html(self, link)
        print(html)
        return HttpResponse('voshlo')

    def get_html(self, link, params=None):
        r = requests.get(link, params=params)
        return r
