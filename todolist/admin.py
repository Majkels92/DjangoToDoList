from django.contrib import admin
from .models import User, Task
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "email", "nickname"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "deadline", "user", "slug", "description"]
    exclude = ["is_done"]
    prepopulated_fields = {"slug": ("title",)}

