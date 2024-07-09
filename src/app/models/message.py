from django.db import models


class Message(models.Model):
    conversation = models.ForeignKey(
        to="app.Conversation",
        on_delete=models.CASCADE,
        related_name="messages",
    )
    user = models.ForeignKey(
        to="authentication.User",
        on_delete=models.CASCADE,
    )
    message = models.TextField()  # Security issue if message not encrypted
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return f"{self.message} ({self.conversation.slug})"
