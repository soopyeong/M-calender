from django.contrib import admin
from . import models


@admin.register(models.Calendar)
class CalendarAdmin(admin.ModelAdmin):

    """Calendar Admin"""

    pass
