from multiprocessing.spawn import import_main_path
from django.contrib import admin
from .models import ContactModel
# Register your models here.
admin.site.register(ContactModel)