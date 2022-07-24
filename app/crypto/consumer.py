"""Consumer Crypto"""
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CryptoConsumer(AsyncWebsocketConsumer):
    """Conecxao do websocket na sua aplicaçao
    Ligando a applicação aos grupos definidos como channels_layer

    Args:
        AsyncWebsocketConsumer ():acesso do websock pela url e aos grupos
    """
    async def connect(self):
        await self.channel_layer.group_add('crypto', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard('crypto', self.channel_name)

    async def send_new_data(self, event):
        """Send new Data to queue redis"""
        new_data = event['text']
        await self.send(json.dumps(new_data))
