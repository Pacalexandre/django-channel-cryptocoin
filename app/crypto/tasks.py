"""tarefas"""
from django.conf import settings
import requests
from asgiref.sync import async_to_sync
from django.forms.models import model_to_dict
from celery import shared_task
from channels.layers import get_channel_layer
from .models import Coin

#criando um sincronismo de asyncono to sync
channel_layer = get_channel_layer()


@shared_task
def get_coins_data():
    """Tarefa para buscar as crypto e carregalas na fila do redis """
    uri='coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    url = f'{settings.URL_COINS}{uri}'
    # vamos recupera os dados e salvar no banco de dados
    data = requests.get(url).json()

    #lista de coins atualizada para envio da fila
    coins = []
    # varrendo o resultado da consulta da API vamos fazer uma gravação em nossa model
    # utilizadno a função create_or_insert a função retorno uma tupla obj, bool
    for coin in data:
        objeto, created = Coin.objects.get_or_create(symbol=coin['symbol'])

        #testando o objeto de criação se teve sucesso ou não
        if created:
            print(f'Registro Criado {created}')

        objeto.name = coin['name']
        objeto.symbol = coin['symbol']
        objeto.rank = coin['market_cap_rank']

        #verificando se o preco da crypto foi alterado antes da gravaçao
        #para enviar para a fila a informação alterada
        if objeto.price > coin['current_price']:
            state = 'fall'
        elif objeto.price == coin['current_price']:
            state = 'same'
        elif objeto.price < coin['current_price']:
            state = 'raise'

        objeto.price = coin['current_price']
        objeto.image = coin['image']
        objeto.save()

        new_data = model_to_dict(objeto)
        new_data.update({'state':state})

        coins.append(new_data)

    async_to_sync(channel_layer.group_send)('crypto',{'type': 'send_new_data', 'text':coins})
