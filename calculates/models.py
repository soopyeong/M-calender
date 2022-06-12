from django.db import models


class Calculate(models.Model):

    """Calculate Data Model"""

    CALCULATE_SYMBOL = "symbol"

    CALCULATE_CHOICES = ((CALCULATE_SYMBOL, "심볼"),)


class Symbol(models.Model):

    """Symbol Data Models"""

    SYMBOL_ARCANE = "arcane"
    SYMBOL_AUTHENTIC = "authentic"

    SYMBOL_CHOICES = (
        (SYMBOL_ARCANE, "아케인"),
        (SYMBOL_AUTHENTIC, "어센틱"),
    )

    ARCANE_JOURNEY = "journey"
    ARCANE_CHUCHU = "chuchu"
    ARCANE_LACHELN = "lacheln"
    ARCANE_ARCANA = "arcana"
    ARCANE_MORAS = "moras"
    ARCANE_ESFERA = "esfera"

    ARCANE_CHOICES = (
        (ARCANE_JOURNEY, "여로"),
        (ARCANE_CHUCHU, "츄츄"),
        (ARCANE_LACHELN, "레헬른"),
        (ARCANE_ARCANA, "아르카나"),
        (ARCANE_MORAS, "모라스"),
        (ARCANE_ESFERA, "에스페라"),
    )

    AUTHENTIC_CERNIUM = "cernium"
    AUTHENTIC_ARCUS = "arcus"

    AUTHENTIC_CHOICES = (
        (AUTHENTIC_CERNIUM, "세르니움"),
        (AUTHENTIC_ARCUS, "아르크스"),
    )

    symbol_kind = models.CharField(max_length=10, choices=SYMBOL_CHOICES)
    arcane_symbol_kind = models.CharField(
        max_length=10, choices=ARCANE_CHOICES, blank=True
    )
    authentic_symbol_kind = models.CharField(
        max_length=10, choices=AUTHENTIC_CHOICES, blank=True
    )
    max_daily_acquisition = models.IntegerField()
