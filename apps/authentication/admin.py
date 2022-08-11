from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SchoolEmail, SchoolModel, CustomSchoolUser
# Register your models here.
admin.site.register(SchoolModel)
admin.site.register(CustomSchoolUser)
admin.site.register(SchoolEmail)
