from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SchoolModel, CustomSchoolUser

# Register your models here.
admin.site.register(SchoolModel)
admin.site.register(CustomSchoolUser)

