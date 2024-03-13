# Topic - Chat App with Static -Group Name
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json

class MyAsyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('programmers', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('programmers', self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        await self.channel_layer.group_send(
            'programmers',
            {
                'type': 'chat.message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
