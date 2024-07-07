from django.db import models


class Message(models.Model):
    room = models.ForeignKey(
        to="app.Room",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to="authentication.User",
        on_delete=models.CASCADE,
    )
    message = models.TextField()  # Security issue if message is not encrypted
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return f"{self.message} ({self.room.name})"
