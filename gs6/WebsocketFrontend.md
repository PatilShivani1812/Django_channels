*******WebSocket
The Websocket object provides the API for creating and managing a websocket connection to a server, as well as for sending and receiving data on the connection.
To construct a Websocket,use the Websocket() constructor.
Example:-
var ws = new WebSocket('ws://127.0.0.1:8000/ws/sc');

****WebSocket Properties
+ onopen - The websocket.onopen property is an event handler that is called when the websocket connection's readyState changes to 1; this indicates that the connection is ready to send and receive data.It is called with an event.
Example:-
ws.onopen = function(event){
    console.log("websocket connection open",event);
};

+ onmessage - The WebSocket.onmessage property is an event handler that is called when a message is received from the server.It is called with a MessageEvent.
Example:-
ws.onmessage = function(event){
    console.log("WebSoket message received from server",event);
};

+ onerror - The WebSocket interface's onerror event handler property is a function which gets called when an error occurs on the websocket.
Example:-
ws.onerror = function(event){
    console.log("Websocket Error Occurred",event);
};

+ onclose - The WebSocket.onclose property is an event handler that is called when the WebSocket connection's readyState Changes to CLOSED. It is called with a CloseEvent.
Example:-
ws.onclose = function(event){
    console.log("WebSocket connection Closed",event);
};
+ binaryType
+ bufferedAmount 
+ extensions
+ protocol
+ readyState
+ url

***Events
& open - The open event is fired when a connection with a WebSocket is opened 
Example:-
ws.addEventListener('open',(event)=>{
    console.log("WebSocket Connection open");
});

& message - The message event is fired when data is received through a WebSocket.
Example : -
ws.addEventListener('message',(event)=>{
    console.log('WebSocket message received from server',event);
});

& error - The error event is fired when a connection with a WebSocket has been closed due to an error.
Example:-
ws.addEventListener('error',(event)=>{
    console.log("W  ebSocket Error Occurred",event);

});

& close - The close event is fired when a connection with a WebSocket is closed.
Example:-
ws.addEventListener('close',(event)=>{
    console.log('WebSocket connection Closed',event);
});

****Methods
+ close() - The WebSocket.close() method closes the WebSocket connection or connection attempt, if any. If the connection is already CLOSED, this method does nothing.
Syntax : -ws.close(code,reason)

code - A numeric value indicating the status code explaining why the connection is being closed. If this parameter is not specified ,a default value of 1005 is assumed.see the list of status codes of CloseEvent for permitted values.
reason - Ahuman-readable string explaining why the connection is closing . This string must be no longer than 123 bytes of UTF-8 text(not characters).
Example : -ws.close()

+ send()- the WebSocket.send() method enqueues the specified data to be transmitted to the server over the WebSocket connection, increasing the value of bufferedAmount by the number of bytes needed to contain the data.

If the data can't be sent ,the socket is closed automatically.
the browser will throw an exception if you call send() when the connection is in the CONNECTING state.
If you call send() when the connection is in the CLOSING or CLOSED states, the browser will silently discard the data.
Syntax : -ws.send(data)
Example:-ws.send("Hello")

***readyState
value       State              Description
0         CONNECTING        Socket has been created. The connection is not yet open.
1         OPEN              The connection is open and ready to communicate.
2         CLOSING           The connection is in the process of closing.
3         CLOSED            The connection is closed or couldn't be opened. 
