import uuid
from unicodedata import name
from .utils import generate_random_id
from django.db import models  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=45)

class Student_Id(models.Model):
    Student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Email(models.Model):
    Email = models.EmailField(max_length=245)


class Debt(models.Model):
    Debt = models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
    return "#" + str(Debt)


class AmountPaid(models.Model):
    AmountPaid = models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
    return "#" + str(AmountPaid)


STATUS_LIST = (
    ('Active', 'Active'),
    ('Pending', 'Pending'),
    ('Resolved', 'Resolved'),
    )
    
class Status(models.Model):
    status = models.CharField(max_length=50, choices=STATUS_LIST)


    


