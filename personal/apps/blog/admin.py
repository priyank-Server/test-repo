from django.contrib import admin
from .models import *


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['word', 'slug', 'description']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['word', 'slug', 'description']






