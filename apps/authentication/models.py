from difflib import IS_CHARACTER_JUNK
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

class SchoolEmail(models.Model):
    email = models.EmailField(null=False, unique=True)

    def __str__(self):
        return self.email

class SchoolModel(models.Model):
    school_name = models.CharField(max_length=200)
    email = models.OneToOneField(SchoolEmail, on_delete=models.CASCADE)
    administrator_name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.PositiveIntegerField()
    zip_code = models.PositiveIntegerField()
    cac_reg_number = models.PositiveIntegerField()
    school_image = models.ImageField(upload_to=filepath)
    cerificate_image = models.ImageField(upload_to=filepath)

    def __str__(self):
        return self.school_name 

class CustomSchoolUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        # if not email:
        #     raise ValueError("Email is required")

        # user = self.model(
        #     email= self.normalize_email(email),
        # )
        # user.set_password(password)
        # user.save(using=self._db)
        # return user
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
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

        user = self.model(
            email = self.normalize_email(email)
        )

        user.is_staff = True
        user.is_superuser = True

        return self.create_superuser(email, password,)

class CustomSchoolUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(verbose_name="email address", unique=True)
    slug = models.SlugField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomSchoolUserManager()

# class CustomSchoolUser(AbstractUser):
#     school_email = models.EmailField(max_length=300, blank=False)
#     school_name = models.CharField(max_length=200, blank=False)
#     school_administrator = models.CharField(max_length=500, blank=False)
#     school_address = models.CharField(max_length=200, blank=True,)
#     phone_number = models.CharField(max_length=15, blank=True)
#     zip_code = models.CharField(max_length=200, blank=True)
#     cac_reg = models.IntegerField(blank=False)
#     verification_code = models.IntegerField(blank=False, unique=True)
#     school_photo = models.FileField(max_length=200, blank=False)
    
    


#     pass
#     # add additional fields in here

#     def __str__(self):
#         return self.username