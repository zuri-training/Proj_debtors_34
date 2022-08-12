
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import forms
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("school_email", "school_name", "password","confirm_password", "school_administrator", "school_address", "phone_number", "zip_code", "cac_reg", "verification_code", "school_photo")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("school_email", "school_name","password","confirm_password", "school_administrator", "school_address", "phone_number", "zip_code", "cac_reg", "verification_code", "school_photo")