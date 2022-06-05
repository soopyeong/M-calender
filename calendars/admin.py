from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Calendar)
class CalendarAdmin(admin.ModelAdmin):

    """Calendar Admin"""

    pass
