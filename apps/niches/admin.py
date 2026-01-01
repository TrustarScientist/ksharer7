from django.contrib import admin

# to register the Niche model in the admin site
from .models import Niche

class NicheAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'is_predefined', 'is_private', 'created_at')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Niche, NicheAdmin)

