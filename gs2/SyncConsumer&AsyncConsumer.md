****Consumers*****
A consumer is the basic unit of Channels code.Consumers are like Django views.
Consumers do following things in particular:
Structures your code as a series of functions to be called whenever an event happens,rather than making you write an event loop.
Allow you to write synchronous or async code and deals with handoffs and threading for you.

Creating Consumers:-
SyncConsumer
AsyncConsumer

**** Creating Consumers
A consumer is a subclass of either SyncConsumer or AsyncConsumer.
SyncConsumer will run your code synchronously in a threadpool.

app/consumers.py
from channels.consumer import SyncConsumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("WebSocket Connect....") 
    # This handler is called when client initially opens a connection and is about to finish the websocket handshake.

    def websocket_receive(self,event):
        print("Websocket Received....")
    # This handler is called when data received from client


    def websocket_disconnect(self,event):
        print("websocket Disconnect...")
    # This handler is called when either connection to the client is lost ,either from the client closing the connection, the server closing the connection, or loss of the socket.

AsyncConsumer will expect you to write async-capable code.
app/consumers.py
from channels.consumer import AsyncConsumer

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("Websocket connected...")
    async def websocket_receive(self,event):
        print("Websocket Received...")
    async def websocket_disconnect(self,event):
        print("websocket Disconnect...")
        



