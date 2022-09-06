from django.contrib import admin
from apps.snippet import models


@admin.register(models.Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
