from django.urls import path
from .consumers import *

websocket_urlpatterns=[
    path('ws/<str:connection>/' , EcoSystemConsumer.as_asgi()),
]