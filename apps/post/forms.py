from django import forms
from .models import post

class postForm(forms.Modelform):
    class Meta:
        model = post
        fields = [
            "Name"
            "Student_ID"
            "Email"
            "Debt"
            "Amount_Paid"
            "Status"
        ]