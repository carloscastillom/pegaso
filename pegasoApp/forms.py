from django import forms
from .models import taskDB

class TaskForm(forms.ModelForm):
    class Meta:
        model = taskDB
        fields = ['task', 'priority', 'status']