from django.contrib import admin

from core.models import Profile, Email

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    ) # tuple of column names
    search_fields = (
        "name",
    )

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = (
        "email",
    )