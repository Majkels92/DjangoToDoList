from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    # Task.deadline = forms.DateTimeField(input_formats=['d.m.Y, H:i'])
    class Meta:
        model = Task
        exclude = ["add_time", "is_done"]
