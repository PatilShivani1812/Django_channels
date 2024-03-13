****Routing 
Channels provides routing classes that allow you to combine and stack your consumers (and any other valid ASGI application) to dispatch based on what the connection is.
we call the as_asgi() classmethod when routhing our consumers.
This returns an ASGI wrapper application that will instantiate a new consumer instance for each connection or scope.
This is similar t django's as_view(),which plays the same role for per-request instances of class-based views.
-Create routing.py file then write all websocket url patterns inside this file.
-open asgi.py file and mentioned your routing.py file.

app/routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sc/', consumers.MySyncConsumer.as_asgi()),
    path('ws/ac/',consumers.MyAsyncConsumer.as_asgi()), 
]

gs3/asgi.py

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