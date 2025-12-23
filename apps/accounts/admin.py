from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User

    list_display = (
        "username",
        "email",
        "phone",
        "is_verified",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "is_staff",
        "is_active",
        "is_verified",
        "groups",
    )

    search_fields = ("username", "email", "phone")

    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email", "phone")}),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "phone",
                "password1",
                "password2",
                "is_staff",
                "is_active",
            ),
        }),
    )
