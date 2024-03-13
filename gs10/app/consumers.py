# Topic - Chat App with Static -Group Name
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import SyncConsumer
from asgiref.sync import sync_to_async
import json

class MyAsyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("group name....", group_name)
        await self.channel_layer.group_add(group_name, self.channel_name)
        await self.accept()
        self.group_name = group_name


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        await self.channel_layer.group_send(
            self.group_name,
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

### Not working ###

# class MySyncConsumer(SyncConsumer):
#     def connect(self):
#         group_name = self.scope['url_route']['kwargs']['groupkaname']
#         print("Group name:", group_name)
#         self.channel_layer.group_add(group_name, self.channel_name)
#         self.accept()
#         self.group_name = group_name

#     def disconnect(self, close_code):
#         self.channel_layer.group_discard(self.group_name, self.channel_name)

#     def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data['message']
#         self.channel_layer.group_send(
#             self.group_name,
#             {
#                 'type': 'chat.message',
#                 'message': message
#             }
#         )

#     def chat_message(self, event):
#         message = event['message']
#         self.send(text_data=json.dumps({
#             'message': message
#         }))

