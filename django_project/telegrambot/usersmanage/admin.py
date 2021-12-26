from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "user_id", "access", "name", "username", "language", "created_at", "updated_at")
    list_filter = ['created_at', 'updated_at']
    list_display_links = ("user_id", "name")
    search_fields = ('name', 'username')
    list_editable = ["access"]
