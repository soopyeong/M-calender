from django.contrib import admin
from . import models


@admin.register(models.SymbolData)
class SymbolDataAdmin(admin.ModelAdmin):

    """Symbol data admin"""

    pass
