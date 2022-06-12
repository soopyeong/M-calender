from django.contrib import admin
from . import models


@admin.register(models.Calculate, models.Symbol)
class CalculateAdmin(admin.ModelAdmin):

    """Calculate Admin"""

    pass
