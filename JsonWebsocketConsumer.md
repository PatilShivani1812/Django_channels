******* Generic Consumer
Channels ships with generic consumers that wrap common functionality up so you don't need to rewrite it, specifically for HTTP and WebSocket handling.
 - WebsocketConsumer
 - AsyncWebsocketConsumer
 - JsonWebsocketConsumer
 - AsyncJsonWebsocketConsumer

***JsonWebsocketConsumer
This works like WebsocketConsumer,except it will auto-encode and decode to JSON sent as WebSocket text frames.

from channels.generic.websocket import JsonWebsocketConsumer
class MYJsonWebsocketConsumer(JsonWebsocketConsumer):
    pass
*** method
+ connect(self) - This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
+ receive_json(self,content,**kwargs) - This handler is called when data received from Client.This method must take a single argument, content,that is the decoded JSON object.
+ disconnect(self,close_code) - This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
+ accept() - This is used to accept the connection.
accept(supprotocol") - This is used to accept the connection and specify a chosen subprotocol.
+ close() - This is used to reject the connection.
close(code = 4123) - This is used to reject connection with custom websocket error code.
+ send_json(content)- this is used to Encode the given content as JSON and send it to the client.

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    def connect(self):
        print("websocket connected...)

        self.accept()

    def receive_json(self,content,**kwargs):
        print("message Received from client...",content)
        self.send_json({
            'message':'message sent to client',
        })
    def disconnect(self,close_code):
        print("websocket Disconnected...',close_code)

****AsyncJsonWebsocketConsumer
+ This has the exact same methods and signature as JsonWebsocketConsumer but everything is async,and the functions you need to write have to be as well.

class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    pass

*** Methods

+ connect(self) - This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
+ receive_json(self,content,**kwargs) - This handler is called when data received from Client.This method must take a single argument, content,that is the decoded JSON object.
+ disconnect(self,close_code) - This handler is called when either connection to the client is lost, either from the client closing the connection, the server closing the connection, or loss of the socket.
+ accept() - This is used to accept the connection.
accept(supprotocol") - This is used to accept the connection and specify a chosen subprotocol.
+ close() - This is used to reject the connection.
close(code = 4123) - This is used to reject connection with custom websocket error code.
+ send_json(content)- this is used to Encode the given content as JSON and send it to the client.


class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("websocket connected..')
        await self.accept()
    async def receive_json(self,content,**kwargs):
        print("Message Received from client..',content)
        await self.send_json({
            'message':"Message sent to client"
        })
    async def disconnect(self,close_code):
        print('websocket Disconnect...',close_code)
