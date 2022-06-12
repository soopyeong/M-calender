from django.db import models

# Create your models here.


class Calendar(models.Model):

    """Calendar Models"""

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="calendar"
    )
    title = models.CharField(max_length=30, default="")
    description = models.TextField(default="")


class Symbol(models.Model):

    """Symbol models"""

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="symbol_calendar"
    )
    symbol_calc_data = models.OneToOneField("data.SymbolData", on_delete=models.CASCADE)
