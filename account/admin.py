from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .custom_user_forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["username", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["username", "password"]}),
        ("Permissions", {"fields": ["is_admin", "is_active"]}),
    ]

    add_fieldsets = [
        (None, {"fields": ["username", "password1", "password2"]}),
        ("Permissions", {"fields": ["is_admin", "is_active"]}),
    ]

    search_fields = ["username"]
    ordering = ["created"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
