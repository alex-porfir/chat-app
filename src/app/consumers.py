import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from app.models import Message, Conversation


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.conversation_name = self.scope["url_route"]["kwargs"]["conversation_slug"]
        self.conversation_group_name = "conversation_%s" % self.conversation_name
        self.user = self.scope["user"]

        await self.channel_layer.group_add(
            self.conversation_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.close_conversation(self.conversation_name, self.user)

        await self.channel_layer.group_discard(
            self.conversation_group_name, self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        user = self.user
        username = user.username
        conversation = self.conversation_name

        # Persist the message
        await self.save_message(conversation, user, message)

        await self.channel_layer.group_send(
            self.conversation_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        current_user = self.user.username

        message_html = f"<div hx-swap-oob='beforeend:#messages'><div class='border-start border-primary border-3 bg-secondary-subtle rounded mb-3 mx-3'><p class='m-0 text-msg'><div class='ps-2 fw-bold'>{username}</div><div class='ps-2 text-muted'>{message}</div></div></div>"

        await self.send(
            text_data=json.dumps(
                {
                    "message": message_html,
                    "username": username,
                },
            )
        )

    @sync_to_async
    def save_message(self, slug, user, message):
        conversation = Conversation.objects.get(slug=slug)
        Message.objects.create(conversation=conversation, user=user, message=message)

    @sync_to_async
    def close_conversation(self, slug, user):
        conversation = Conversation.objects.get(slug=slug)
        conversation.new = False
        conversation.save()
