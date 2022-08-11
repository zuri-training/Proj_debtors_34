from dataclasses import fields
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import forms
from .models import CustomSchoolUser
from django import forms
from django.contrib.auth import authenticate

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label='password')
    class Meta:
        model = CustomSchoolUser()
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid credentials! Try again.")

    widgets ={
        'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        'password': forms.PasswordInput(attrs={'class': 'form-control'}),
    }
            

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ("school_email", "school_name", "school_administrator", "school_address", "phone_number", "zip_code", "cac_reg", "verification_code", "school_photo")
        

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ("school_email", "school_name", "school_address", "phone_number", "zip_code", "cac_reg", "verification_code", "school_photo")