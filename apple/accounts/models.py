from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    id_number = models.IntegerField(null=True)
