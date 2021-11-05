from django.urls import path
from .views import *

urlpatterns = [
    path('', GetLinkView.as_view(), name='get_link')
]