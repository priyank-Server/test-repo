from django.contrib import admin
from apps.contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email']





