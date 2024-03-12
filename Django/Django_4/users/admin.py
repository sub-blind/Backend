from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib import admin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_business", "grade")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
