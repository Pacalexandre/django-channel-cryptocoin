"""Configurando rotas de websocket"""
from django.urls import path
from .consumer import CryptoConsumer

#class que define as rotas do websocket
ws_urlpatterns = [
    path('ws/crypto/', CryptoConsumer.as_asgi())
]