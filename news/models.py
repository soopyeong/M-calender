from django.db import models

# Create your models here.


class News(models.Model):

    """News model"""

    class Meta:
        verbose_name_plural = "News"

    NOTICE_NOTICE = "notice"
    NOTICE_INSPECTION = "inspection"
    NOTICE_EVENT = "event"

    NOTICE_CHOICES = (
        (NOTICE_NOTICE, "공지"),
        (NOTICE_INSPECTION, "점검"),
        (NOTICE_EVENT, "이벤트"),
    )

    title = models.CharField(max_length=100)
    notice_kind = models.CharField(max_length=12, choices=NOTICE_CHOICES)
    link = models.URLField()
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.title
