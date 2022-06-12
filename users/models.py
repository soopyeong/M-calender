from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """Custom User Model"""

    LOGIN_GOOGLE = "google"
    LOGIN_NAVER = "naver"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_GOOGLE, "구글"),
        (LOGIN_NAVER, "네이버"),
        (LOGIN_KAKAO, "카카오"),
    )

    login_method = models.CharField(max_length=10, choices=LOGIN_CHOICES)
