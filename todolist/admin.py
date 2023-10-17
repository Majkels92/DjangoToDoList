from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Task
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["name", "surname", "email", "nickname"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "deadline", "user", "description"]
    exclude = ["is_done"]


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "first_name", "last_name"]


admin.site.register(CustomUser, CustomUserAdmin)
