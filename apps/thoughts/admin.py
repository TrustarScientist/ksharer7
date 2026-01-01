from django.contrib import admin

# to register the Thought model in the admin site
from .models import Thought
class ThoughtAdmin(admin.ModelAdmin):
    list_display = ('author', 'niche', 'is_pinned', 'created_at')
    list_filter = ('is_pinned', 'created_at', 'niche')
    search_fields = ('content', 'author__username', 'niche__name')

admin.site.register(Thought, ThoughtAdmin)


