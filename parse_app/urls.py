from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', do_logout, name='logout'),
    path('', GetLinkView.as_view(), name='get_link')
]