from dataclasses import fields
import imp
from django import forms
from django.forms import ModelForm
from .models import Message

class MessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "forms", "rows": 2, "placeholder": "Enter message"}))
    class Meta:
        model = Message
        fields = ["body", ]