from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    profile_img = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username


class Puns(models.Model):
    post = models.CharField(max_length=200)
    date_posted = models.DateTimeField()
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='puns'
    )

# class Badge(models.Model):
#     image = models.URLField()
#     user = models.ManyToManyField(CustomUser, related_name="badges")
#     description = models.TextField()
# not sure if i want to use a badge ...