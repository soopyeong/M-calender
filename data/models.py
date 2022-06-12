from django.db import models

# Create your models here.


class SymbolData(models.Model):

    """Symbol Personal Data"""

    class Meta:
        verbose_name_plural = "Symbol Data"

    user = models.OneToOneField(
        "users.User", on_delete=models.CASCADE, related_name="symbol_data"
    )
