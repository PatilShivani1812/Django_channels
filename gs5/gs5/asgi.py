"""
ASGI config for gs5 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from app import routing as app_routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs4.settings')

django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    "http" : django_asgi_app,
    'websocket' : URLRouter(
        app_routing.websocket_urlpatterns
    )

})