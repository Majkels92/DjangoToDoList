from django import forms
from .models import Task, CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["add_time", "is_done"]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'enter title here...'}),
            'deadline': forms.TextInput(attrs={'placeholder': 'd.m.y h:m'}),
            'description': forms.Textarea(attrs={'placeholder': 'enter description here...',
                                                 'rows': '8'}),
        }
