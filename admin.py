from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["school_email", "school_name", "password","confirm_password", "school_administrator", "school_address", "phone_number", "zip_code", "cac_reg", "verification_code", "school_photo"]

    

admin.site.register(CustomUser, CustomUserAdmin)