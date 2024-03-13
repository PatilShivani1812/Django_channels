# # Topic - Database

# from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import sync_to_async
# from .models import Chat, Group
# import json
# from channels.db import database_sync_to_async

# class MyAsyncConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.group_name = self.scope['url_route']['kwargs']['groupkaname']
#         print("group name....", self.group_name)
#         await self.channel_layer.group_add(self.group_name, self.channel_name)
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.group_name, self.channel_name)

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data['message']
#         print(self.scope['user'])# find user 
#         group = await self.get_group(self.group_name)
#         if self.scope['user'].is_authenticated:
#             chat = await self.create_chat(message, group)
#             await database_sync_to_async(chat.save)()

#             await self.channel_layer.group_send(
#                 self.group_name,
#                 {
#                     'type': 'chat.message',
#                     'message': message
#                 }
#             )
#         else:
#             self.send({
#                 'type':'websocket.send',
#                 'text': json.dumps({"message":"Login Required"})
#             })

#     async def chat_message(self, event):
#         message = event['message']
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))

#     @sync_to_async
#     def get_group(self, group_name):
#         return Group.objects.get(name=group_name)

#     @sync_to_async
#     def create_chat(self, message, group):
#         return Chat.objects.create(content=message, group=group)


# New
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chat, Group
import json
from channels.db import database_sync_to_async

class MyAsyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("group name....", self.group_name)
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        print("username...",self.scope['user'])
        username = self.scope['user'].username if self.scope['user'].is_authenticated else 'Anonymous' # find user 
        print(f"Received message from {username}: {message}") 
        group = await self.get_group(self.group_name)
        if self.scope['user'].is_authenticated:
            chat = await self.create_chat(message, group)
            await database_sync_to_async(chat.save)()
            # data["user"] = self.scope["user"].username
            # print("complete Data",data)
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'chat.message',
                    'username': username,
                    'message': message
                }
            )
        else:
            await self.send(text_data=json.dumps({"message": "Login Required","username":"guest"}))

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def get_group(self, group_name):
        return Group.objects.get(name=group_name)

    @database_sync_to_async
    def create_chat(self, message, group):
        return Chat.objects.create(content=message, group=group)



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

