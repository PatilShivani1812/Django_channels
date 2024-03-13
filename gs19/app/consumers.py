# Topic - Generic Consumer - JsonWebsocketConsumer and AsyncJsonWebsocketConsumer
# Real- time Data Example
# Real-time Data Example with Front End.
from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer
from time import sleep
import asyncio

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
   #This handler is called when client initially opens a connection and is about to finish the Websocket handshake.
    def connect(self):
        print("websocket connected...")
        self.accept()       # To accept the connection 
  

    # this handler is called when data received from client with decoded JSON content.
    def receive_json(self,content,**kwargs):
        print("message received from client...",content)
        # Encode the given content as JSON and send it to the client.
        for i in range(20):
            self.send_json({
            'message':str(i)
        })
            sleep(1)


    # this handler is called when either connection to the client is lost, either from the client closing the connection,the server closing the connection, or loss of the socket.
    def disconnect(self,close_code):
        print('websocket Disconnected...',close_code)


class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
   #This handler is called when client initially opens a connection and is about to finish the Websocket handshake.
    async def connect(self):
        print("websocket connected...")
        await self.accept()       # To accept the connection 


    # this handler is called when data received from client with decoded JSON content.
    async def receive_json(self,content,**kwargs):
        print("message received from client...",content)
        # Encode the given content as JSON and send it to the client.
        for i in range(20):
            await self.send_json({
            'message':str(i)
        })
            await asyncio.sleep(1)




    # this handler is called when either connection to the client is lost, either from the client closing the connection,the server closing the connection, or loss of the socket.
    async def disconnect(self,close_code):
        print('websocket Disconnected...',close_code)
