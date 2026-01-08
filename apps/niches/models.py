from django.db import models

# Create your models here.
class Niche(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    # short tag description such as @webdev, #python
    alias = models.CharField(max_length=10, blank=True)
    is_predefined = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
