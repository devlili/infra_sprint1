from django.contrib import admin

from .models import Achievement, Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "color",
        "birth_year",
        "owner",
        "image",
    )
    search_fields = ("name",)
    list_filter = ("birth_year",)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")
    search_fields = ("name",)
