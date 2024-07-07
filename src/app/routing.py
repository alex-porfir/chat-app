from django.urls import path

from app import consumers

websocket_urlpatterns = [
    path("chat/<str:room_slug>/", consumers.ChatConsumer.as_asgi()),
]
