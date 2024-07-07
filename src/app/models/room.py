from django.db import models


class Room(models.Model):
    name = models.CharField(
        max_length=128,
    )
    slug = models.SlugField(
        unique=True,
    )
    users = models.ManyToManyField(
        to="authentication.User",
    )

    def __str__(self) -> str:
        return f"{self.name}"
