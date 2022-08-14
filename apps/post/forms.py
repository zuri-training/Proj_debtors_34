from django import forms
from .models import Comment

class ComentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')