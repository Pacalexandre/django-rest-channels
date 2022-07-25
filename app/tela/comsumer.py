import json
from channels.generic.websocket import AsyncWebsocketConsumer


class TelaComsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add('processo', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard('processo', self.channel_name)
        await self.close(code)

    async def create_processo(self, event):
        print(event['text'])
        await self.send(json.dumps(event['text']))
