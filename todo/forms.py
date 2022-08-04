from email.policy import default
from statistics import mode
from todo.models import task
from django import forms

class input_task(forms.ModelForm):
    task_text=forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class': "form-input"}))
    class Meta:
        model=task
        fields=['task_text']