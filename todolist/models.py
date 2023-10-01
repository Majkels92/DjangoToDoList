from django.db import models


class User(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=120)
    email = models.EmailField()
    nickname = models.CharField(max_length=100)


class Task(models.Model):
    title = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    slug = models.SlugField()
    description = models.TextField()
