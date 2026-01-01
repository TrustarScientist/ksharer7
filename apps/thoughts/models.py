from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Thought(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="thoughts")
    niche = models.ForeignKey("niches.Niche", on_delete=models.CASCADE, related_name="thoughts")

    content = models.TextField(max_length=500)

    is_pinned = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
