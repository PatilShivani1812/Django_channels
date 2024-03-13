"""
ASGI config for gs22 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from app import routing as app_routing
from channels.auth import AuthMiddlewareStack

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs8.settings')

# Get the Django ASGI application
django_asgi_app = get_asgi_application()

# Define the application routing
application = ProtocolTypeRouter({
    "http": django_asgi_app,  # HTTP requests are handled by the Django ASGI application
    'websocket': AuthMiddlewareStack(
        URLRouter(
            app_routing.websocket_urlpatterns  # Routes WebSocket connections to appropriate consumers
        )
    )
    
})