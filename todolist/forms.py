from django import forms
from .models import Task


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
