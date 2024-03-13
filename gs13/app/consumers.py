# Topic - Generic Consumer - WebsocketConsumer and AsyncWebsocketConsumer

from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer

class MyWebsocketConsumer(WebsocketConsumer):
    # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
    def connect(self):
        print("WebSocket Connected...")
        self.accept()       # To accept the connection
        # await self.close()        # To reject the connection
    # This handler is called when data received from Client.
    def receive(self,text_data= None,bytes_data =None):
        print("Message Received from client...",text_data)
        self.send(text_data ="Message from server to client")   #To send Data to Client
        # self.send(bytes_data = data)  # To send Binary Frame to Client. 
        # self.close()   # To force-close the connection.
        # self.close(code = 4123)  # To add a custom websocket error code 
    #This handler is called when either connection to the client is lost,either from the client closing the connection ,the server closing the connection, or loss of the socket.
    def disconnect(self,close_code):
        print("Websocket Disconnected...",close_code)  



class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    # This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
    async def connect(self):
        print("WebSocket Connected...")
        await self.accept()       # To accept the connection
        # await self.close()        # To reject the connection
    # This handler is called when data received from Client.
    async def receive(self,text_data= None,bytes_data =None):
        print("Message Received from client...",text_data)
        await self.send(text_data ="Message from server to client")   #To send Data to Client
        # await self.send(bytes_data = data)  # To send Binary Frame to Client. 
        # await self.close()   # To force-close the connection.
        # await self.close(code = 4123)  # To add a custom websocket error code 
    #This handler is called when either connection to the client is lost,either from the client closing the connection ,the server closing the connection, or loss of the socket.
    async def disconnect(self,close_code):
        print("Websocket Disconnected...",close_code)  