
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Additional fields if needed
    is_admin = models.BooleanField(default=False)
    is_developer = models.BooleanField(default=False)
    is_qa = models.BooleanField(default=False)

    def __str__(self):
        return self.username
