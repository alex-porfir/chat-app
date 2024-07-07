from django.urls import path
from django.views.generic import TemplateView
from app.views import chat


urlpatterns = [
    path("chat/", TemplateView.as_view(template_name="app/chat.html"), name="index"),
    path("room/<str:slug>/", chat.index, name="chat"),
    path("create/", chat.room_create, name="room-create"),
    path("join/", chat.room_join, name="room-join"),
]
