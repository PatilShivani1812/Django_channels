**** Generic Consumer
Channels ships with generic consumers that wrap common functionality up so you don't need to rewrite it, specifically for HTTP and WebSocket handling.
 - WebsocketConsumer
 - AsyncWebsocketConsumer
 - JsonWebsocketConsumer
 - AsyncJsonWebsocketConsumer

 ***WebsocketConsumer
 This wraps the verbose plain -ASGI message sending and receiving into handling that just deals with text and binary frames.
 from channels.generic.websocket import WebsocketConsumer
 class MyWebsocketConsumer(WebsocketConsumer):
    pass

***Method
+ connect(self) - This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
+ receive(self,text_data = None,bytes_data = None) - This handler is called when data received from Client.
+ disconnect(self,close_code) - This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
+ accept() - This is used to accept the connection.
accept(subprotocol") - This is used to accept the connection and specify a chosen subprotocol.

+ close() - This is used to reject the connection.
close(code = 4123) - This is used to reject connection with custom websocket error code.
+ send(text_data="String")- This is used to send Data to Client.
+ send(bytes_data = data) - This is used to send Binary Frame to Client.

class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("WebSocket Connected...")
        self.accept()

    def receive(self,text_data=None,bytes_data=None):
        print("Message Received from Client....",text_data)
        self.send(text_data = "Hello World !") # Data Sending to Client
    
    def disconnect(self,close_code):
        print("Websocket Disconnect...",close_code)


****AsyncWebsocketConsumer
This has the exact same methods and signature as WebsocketConsumer but everything is async, and the functions you need to write have to be as well.

from channels.generic.websocket import AsyncWebsocketConsumer
class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    pass

class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket Connected...")
        await self.accept()

    async def receive(self,text_data=None,bytes_data=None):
        print("Message Received from Client....",text_data)
        await self.send(text_data = "Hello World !") # Data Sending to Client
    
    async def disconnect(self,close_code):
        print("Websocket Disconnect...",close_code)