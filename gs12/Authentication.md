***Authentication
AuthMiddleware requires Session Middleware to function, which itself requires CookieMiddleware.For convenience, these are also provided as a combined callable  called AuthMiddlewareStack that includes all three.
from channels.auth import AuthMiddlewareStack
application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            app.routing.websocket_urlpatterns
        )
    )
})
To access the user, just use self.scope["user"] in your consumer