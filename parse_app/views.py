from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model

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
