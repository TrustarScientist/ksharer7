from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Core identity model for Ksharer.
    Authentication is handled by Django.
    Authorization is handled via Groups & Permissions.
    """

    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True
    )

    is_verified = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
