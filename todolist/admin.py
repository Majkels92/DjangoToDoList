from django.contrib import admin
from .models import User, Task
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "email", "nickname"]


admin.site.register(User, UserAdmin)
admin.site.register(Task)
