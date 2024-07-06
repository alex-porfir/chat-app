from django.urls import path

from app.views import chat

urlpatterns = [
    path("chat/", chat.chat_view, name="chat"),
]
