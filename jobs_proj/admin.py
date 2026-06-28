from django.contrib import admin
from .models import Vacancy, Article


admin.site.register(Vacancy)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "created_at",
    )

    search_fields = (
        "title",
    )

    ordering = (
        "-created_at",
    )