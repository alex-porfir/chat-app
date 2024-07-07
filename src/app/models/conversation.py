from django.db import models


class Conversation(models.Model):
    slug = models.SlugField(
        unique=True,
    )
    employee = models.ForeignKey(
        to="authentication.User",
        on_delete=models.CASCADE,
        null=False,
        blank=True,
        related_name="customer_support_conversations",
    )
    customer = models.ForeignKey(
        to="authentication.User",
        on_delete=models.CASCADE,
        null=False,
        blank=True,
        related_name="chats",
    )
    new = models.BooleanField(
        default=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.slug}"
