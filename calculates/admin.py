from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Calculate)
class CalculateAdmin(admin.ModelAdmin):

    """Calculate Admin"""

    pass
