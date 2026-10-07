from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'subject', 'description', 'due_date', 'priority', 'status', 'user']
        widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control'}),
    'subject': forms.TextInput(attrs={'class': 'form-control'}),
    'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
    'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    'priority': forms.Select(attrs={'class': 'form-control'}),
    'status': forms.Select(attrs={'class': 'form-control'}),
}