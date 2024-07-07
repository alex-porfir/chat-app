from django.urls import path
from django.views.generic import TemplateView
from app.views import chat


urlpatterns = [
    path(
        "customer_service/",
        chat.customer_service_view,
        name="customer-service",
    ),
    path(
        "connect/", TemplateView.as_view(template_name="app/connect.html"), name="index"
    ),
    path("chat/<str:slug>/", chat.chat, name="chat"),
    path(
        "conversation/initialize/",
        chat.conversation_initialize,
        name="conversation-initialize",
    ),
]
