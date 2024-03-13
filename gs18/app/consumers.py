# Topic - Generic Consumer - JsonWebsocketConsumer and AsyncJsonWebsocketConsumer
from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
   #This handler is called when client initially opens a connection and is about to finish the Websocket handshake.
    def connect(self):
        print("websocket connected...")
        self.accept()       # To accept the connection 
        # self.close()        # To reject the connection

    # this handler is called when data received from client with decoded JSON content.
    def receive_json(self,content,**kwargs):
        print("message received from client...",content)
        print('Type of message received from client..',type(content))

        self.send_json({
            'message':'Message from Server to Client'
        })
        # self.close()        # To force close the connection.

    # this handler is called when either connection to the client is lost, either from the client closing the connection,the server closing the connection, or loss of the socket.
    def disconnect(self,close_code):
        print('websocket Disconnected...',close_code)


class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
   #This handler is called when client initially opens a connection and is about to finish the Websocket handshake.
    async def connect(self):
        print("websocket connected...")
        await self.accept()       # To accept the connection 
        # self.close()        # To reject the connection

    # this handler is called when data received from client with decoded JSON content.
    async def receive_json(self,content,**kwargs):
        print("message received from client...",content)
        print('Type of message received from client..',type(content))

        await self.send_json({
            'message':'Message from Server to Client'
        })
        # await self.close()        # To force close the connection.

    # this handler is called when either connection to the client is lost, either from the client closing the connection,the server closing the connection, or loss of the socket.
    async def disconnect(self,close_code):
        print('websocket Disconnected...',close_code)
