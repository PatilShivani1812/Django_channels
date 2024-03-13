"""
ASGI config for gs2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing  import ProtocalTypeRouter # Import this
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs2.settings')

# application = get_asgi_application()
application = ProtocalTypeRouter({
    'http' : get_asgi_application(),
})