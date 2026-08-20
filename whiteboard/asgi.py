"""
ASGI config for whiteboard project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whiteboard.settings')

asgi_application = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from authentication.middleware import JWTAuthMiddlewareStack
from board.routing import websocket_urlpatterns

application=ProtocolTypeRouter({
    'http':asgi_application,
    'websocket':JWTAuthMiddlewareStack(URLRouter(websocket_urlpatterns))
})
