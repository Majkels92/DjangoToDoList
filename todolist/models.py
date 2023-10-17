from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    is_done = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user")
    slug = AutoSlugField(populate_from='title')
    description = models.TextField()
