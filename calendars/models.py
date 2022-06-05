from django.db import models

# Create your models here.


class Calendar(models.Model):

    """Calendar Model"""

    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
