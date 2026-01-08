from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Thought(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)

    niche = models.ForeignKey(
        "niches.Niche",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="thoughts"
    )

    class Meta:
        ordering = ["-created_at"]

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.content[:30]}"

    

