from difflib import IS_CHARACTER_JUNK
from doctest import BLANKLINE_MARKER
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
import datetime, os

# Create your models here.

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timeNow,old_filename)
    return os.path.join('static/images/school_images',filename)


class CustomSchoolUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
       
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)


        if extra_fields.get("is_staff") is not True:
            raise ValueError("Is staff must be set to true")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Is superuser must be set to true")

        return self.create_user(email, password, **extra_fields)

class CustomSchoolUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="email address", unique=True)
    slug = models.SlugField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomSchoolUserManager()

    def __str__(self):
        return self.email

class SchoolModel(models.Model):
    user = models.OneToOneField(CustomSchoolUser, on_delete=models.CASCADE, null=True, blank=True)
    school_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    administrator_name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.PositiveIntegerField()
    zip_code = models.PositiveIntegerField()
    cac_reg_number = models.PositiveIntegerField()
    school_image = models.ImageField(upload_to=filepath)
    cerificate_image = models.ImageField(upload_to=filepath)

    def __str__(self):
        return self.school_name 
