"""Configurando rotas de websocket"""
from django.urls import path

from .comsumer import TelaComsumer

# class que define as rotas do websocket
ws_urlpatterns = [
    path('ws/tela/', TelaComsumer.as_asgi())
]
