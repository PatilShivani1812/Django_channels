# Topic - Generic Consumer - JsonWebsocketConsumer and AsyncJsonWebsocketConsumer
# Chat app with Dynamic Group Name
from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
   #This handler is called when client initially opens a connection and is about to finish the Websocket handshake.
    def connect(self):
        print("websocket connected...")
        print("channel layer",self.channel_layer)
        print("channel name",self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("Group Name..",self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()       # To accept the connection 
  

    # this handler is called when data received from client with decoded JSON content.
    def receive_json(self,content,**kwargs):
        print("message received from client...",content)
        # Encode the given content as JSON and send it to the client.
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type':'chat.message',
                'message': content['message']
            }

        )
    def chat_message(self,event):
        print('Event...',event)
        self.send_json({
            'message':event['message']
        })



    # this handler is called when either connection to the client is lost, either from the client closing the connection,the server closing the connection, or loss of the socket.
    def disconnect(self,close_code):
        print('websocket Disconnected...',close_code)
        print('Channel Layer',self.channel_layer)
        print('channel Name',self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )


class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
   #This handler is called when client initially opens a connection and is about to finish the Websocket handshake.
    async def connect(self):
        print("websocket connected...")
        print("channel layer",self.channel_layer)
        print("channel name",self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupkaname']
        print("Group Name..",self.group_name)
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()       # To accept the connection 


    # this handler is called when data received from client with decoded JSON content.
    async def receive_json(self,content,**kwargs):
        print("message received from client...",content)
        # Encode the given content as JSON and send it to the client.
        # Encode the given content as JSON and send it to the client.
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'chat.message',
                'message': content['message']
            }

        )
    async def chat_message(self,event):
        print('Event...',event)
        await self.send_json({
            'message':event['message']
        })





    # this handler is called when either connection to the client is lost, either from the client closing the connection,the server closing the connection, or loss of the socket.
    async def disconnect(self,close_code):
        print('websocket Disconnected...',close_code)
        print('Channel Layer',self.channel_layer)
        print('channel Name',self.channel_name)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
