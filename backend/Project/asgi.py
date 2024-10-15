import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from api.middleware import JWTAuthMiddleware
from api import routing as api_routing

# Ensure that the settings module is properly set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')

# Setup Django before importing any models or middleware
django.setup()

# Get the default Django ASGI application
django_asgi_app = get_asgi_application()

# Define the ASGI application for both HTTP and WebSocket protocols
application = ProtocolTypeRouter({
    "http": django_asgi_app,  # Handles HTTP requests
    "websocket": AllowedHostsOriginValidator(
        JWTAuthMiddleware(
            URLRouter(api_routing.websocket_urlpatterns)  # Define WebSocket routing
        )
    ),
})
