from urllib.parse import urlparse

from django.urls import URLPattern
from django.urls import path

app_name = 'app_name'

from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('style/', style, name='style'),
]