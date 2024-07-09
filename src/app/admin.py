from django.contrib import admin

from app.models import Conversation, Message


admin.site.register(Conversation)
admin.site.register(Message)
