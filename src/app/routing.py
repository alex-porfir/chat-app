from django.urls import path

from app import consumers

websocket_urlpatterns = [
    path("conversation/<str:conversation_slug>/", consumers.ChatConsumer.as_asgi()),
]
