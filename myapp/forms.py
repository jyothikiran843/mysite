from dataclasses import fields
from operator import mod
from django import forms
from myapp import models

class Add(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['name','s']