from django.db import models

from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    display_name = models.CharField(max_length=40, null=True, blank=True)
    homepage = models.URLField(max_length=150, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    REQUIRED_FIELDS = ['age']


def __str__(self):
    return self.display_name
