from django.db import models

# Create your models here.


class Calculate(models.Model):

    """Calculate Data Model"""

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
