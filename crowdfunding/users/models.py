from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Badge(models.Model):
    image = models.URLField()
    user = models.ManyToManyField(CustomUser, related_name="badges")
    description = models.TextField()