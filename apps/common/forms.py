from django import forms
from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['email', 'message']
        widgets ={
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }