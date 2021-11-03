from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', do_logout, name='logout'),
    path('get_link/', GetLinkView.as_view(), name='get_link')
]