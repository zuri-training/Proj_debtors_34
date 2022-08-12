from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    school_email = models.EmailField(max_length=300, blank=False)
    school_name = models.CharField(max_length=200, blank=False)
    school_administrator = models.CharField(max_length=500, blank=False)
    school_address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    zip_code = models.CharField(max_length=200, blank=True)
    cac_reg = models.IntegerField(max_length=200, blank=False)
    verification_code = models.IntegerField(max_length=200, blank=False unique=True )
    school_photo = models.FileField(max_length=200, blank=False)
    
    


    pass
    # add additional fields in here

    def __str__(self):
        return self.username