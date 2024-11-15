from django.urls import path
from app1.consumers import ProgressConsumer

websocket_urlpatterns = [
    path("ws/progress/", ProgressConsumer.as_asgi()),
]
