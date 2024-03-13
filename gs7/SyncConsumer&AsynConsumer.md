****Consumers
A consumer is the basic unit of channels code. Consumers are like Django views.
Consumers do a following things in particular:
- Structures your code as a series of functions to be called whenever an event happens, rather than making you write an event loop.
- Allow you to write synchronous or async code and deals with handoffs and threading for you.

**Creating Consumers
A consumer is a subclass of either SyncConsumer or AsyncConsumer.
SyncConsumer will run your code synchronously in a threadpool.
app/consumers.py
from channels.consumer import SyncConsumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
    self.send({
        'type':'websocket.accept'
    })
    def websocket_receive(self,event):
    print("Message received from Client',event['text'])
    self.send({
        'type':'websocket.send',
        'text': 'Message Sent to Client',
    })
    def websocket_disconnect(self,event):
    raise StopConsumer()

AsyncConsumer will expect you to write async-capable code.
app/consumers.py
from channels.consumer import AsyncConsumer
class MyAsyncConsumer(AsyncConsumer):
async def websocket_connect(self,event):
await self.send({'type':'websocket.accept'})
async def websocket_receive(self,event):
print("Message receive from Client",event['text'])
await self.send({
    'type':'websocket.send',
    'text':'Message sent to client',
})
async def websocket_disconnect(self,event):
raise StopConsumer()

+ websocket_connect(self,event) - This handler is called when client initially opens a connection and is about to finish the WebSocket handshake.
+ websocket_received(self,event)
- This handler is called when data received from Client.

+ websocket_disconnect(self,event)
- This handler is called when either connection to the client is lost,either from the client closing the connection, the server closing the connection, or loss of the socket.

Consumers are structured around a series of named methods corresponding to the type value of the messages they are going to receive,with any.replaced by_
Example:-
websockect.connect message is handled by websocket_connect

*****Events
+ Connect - receive event
Sent to the application when the client initially opens a connection and is about to finish the WebSocket handshake.
'type':'websocket.connect'

+ Accept - send event
Sent by the application  when it wishes to accept an incomming connection.
'type':'websocket.accept'
'subprotocol': None
'headers':[name,value] where name is header name and value us header value.

+ Receive - receive event
Sent to the application when a data message is received from the client
'type':'websocket.receive'.
'bytes': None.The message content,if it was binary mode, or None. Optional;if missing ,it is equivalent to None.
'text':None.The message content, if it was text mode,or None,Optional;if missing,it is equivalent to None.

Send- send event
Sent by the application to send a data message to the client.
'type':'websocket.send'.
'bytes':None .This Binary message content,if it was binary mode or None.Optional;if missing ,it is equivalent to None.
'text': None.The Text message content,if it was text mode,or None,Optional,if missing it is equivalent to None.

+ Disconnect - receive event
Sent to the application when either connection to the client is lost ,either from the client closing the connection,the server closing the connection,or loss of the socket.
'type': 'websocket.disconnect'
'code': The WebSocket close code in int,as per the WebSocket spec.

+ close - send event
Sent by the application to tell the server to close the connection.
'type':'websocket.close',
'code':The WebSocket close code inint,as per the WebSocket spec.Optional;if missing defaults to 1000.
'reason': "no need"A reason given for the closure,can be any string.Optional; if missing or None default is empty string.
 
