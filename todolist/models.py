from django.db import models
from autoslug import AutoSlugField


class User(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=120)
    email = models.EmailField()
    nickname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Task(models.Model):
    is_done = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    slug = AutoSlugField(populate_from='title')
    description = models.TextField()
