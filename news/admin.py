from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.News)
class CustomNewsAdmin(admin.ModelAdmin):

    """News Admin"""

    list_display = ("title", "notice_kind", "link", "start", "end")
    list_filter = ("notice_kind",)
