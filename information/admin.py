from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Union, models.Link)
class UnionLinkAdmin(admin.ModelAdmin):

    """Union and Link Admin"""

    list_display = (
        "job",
        "job_first_class",
        "job_second_class",
        "job_group",
        "content",
    )

    list_filter = ("job_first_class", "job_group")
