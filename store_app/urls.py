from django.urls import path
from store_app.views import *

urlpatterns = [
    path('', ShowItemView.as_view(), name='show_item'),


]