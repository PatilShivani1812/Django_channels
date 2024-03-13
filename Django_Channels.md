**WebSocket 
WebSocket is a full duplex(two way communication) protocol that is used in the same scenario of client-server communication.
It is a stateful protocol,which means the connection between client and server will keep alive until it is terminated by either client or server, after closing the connection by either of the client and server,the connection is terminated from both the end.
WebSocket do not use the http://or https:// scheme(because they do not follow the HTTPprotocol).
Rather,WebSocket URLs use a new scheme ws:(orwss: for a sequre websocket).
The remainder of the URL is the same as an HTTP URL: a host,port,path and any query parameters.
Example:-ws://example.com:8000/ws/chat

**How WebSocket Works.

Client ----HTTP Request----> Server
Client <----Handshake--------Server
Client<---WebSocket Two-way communication---->Server
Client---->Close<---------Server

Client sends regular HTTP request with an additional header to be requested.
The Server gets the HTTP request and notices the request for the Upgrade header.This lets the Server know that we are requesting for a websocket connection.
If all goes well persistent connection established between client and server.
connection can be closed either by client or server

***What can we build
chat Application
Real-time Web Application
Notification
Trading
Location Based Application
Real- time Data Visualization
***When use Websocket
WebSocket is not a full -on replacement for the HTTP  protocol so Whenever you need continuously real time data stream over the internet ,whether it be client-to-server or server-to client only they you should use websocket.

***When not to use WebSocket
Whenever you need old data or data only once you should not use websocket rather you should use HTTP protocol.


***AJAX VS WebSocket 
When the traditional request-response is required then ,Ajax can be used.
When there is real-time communication involved and fast results are needed,then web sockets can be used.
In Ajax when you send a request, server sends response for that request and connection ends.
In webSockets when you established  a connection with server,then you can communicate between client and server as much you want and it keeps connection alive.


****Requirements
Python
Django
****How to Install/Uninstall Channels
Install usin pip
    pip install channels

Uninstall using pip
    pip unistall channels

**** Adding Channels to Django Project
INSTALLED_APPS = [
    "daphne",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

*********Configuring asgi.py
import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from app import routing as app_routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': URLRouter(
        app_routing.websocket_urlpatterns )
    # Just HTTP for now. (We can add other protocols later.)
})


ProtocolTypeRouter :-->
    ProtocolTypeRouter lets you dispatch to one of a number of other ASGI applications based on the type value present in the scope.

    Protocol will define a fixed type value that their scope contains, so you can use this to distinguish between incoming connection types.
    ProtocolTypeRouter should be the top level of your ASGI application stack and the main entry in your routing file.
    It takes a single argument - a dictionary mapping type names to ASGI applications that serve them:
    ProtocolTypeRouter({
        "http": django_asgi_app,
        'websocket': URLRouter(
        app_routing websocket_urlpatterns )
    })

******Configuring settings.py

ASGI_APPLICATION = 'gs.asgi.application'


*********Django Channels
Django Channels extends Django's abilities beyond HTTP -to handle websockets ,chat protocols,IOT protocols, and more.
Channels give you the choice to handle other connections in either a synchronous or asynchronous style.
It provides integration with Django's auth system,session system, and more, making it  easier than ever to extend your HTTP-only project to other Protocols.
****Requirements
Python 
Django
