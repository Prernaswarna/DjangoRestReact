from channels.routing import ProtocolTypeRouter , URLRouter
from channels.auth import AuthMiddlewareStack 
import fixer.routing


application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            fixer.routing.websocket_urlpatterns
        )
    ),
    
})
