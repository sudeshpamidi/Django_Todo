from django import forms
from django.forms import ModelForm

from .models import *

class TasksForm(forms.ModelForm):
    """Form defn for Tasks."""

    class Meta:
        """Meta defn for Tasksform."""
        model =Tasks
        fields = "__all__"