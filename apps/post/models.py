import uuid
from unicodedata import name
from .utils import generate_random_id
# from django.utils.translation import ugettext_lazy as _
from django.db import models  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=45)

class Student_Id(models.Model):
    Student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Email(models.Model):
    Email = models.EmailField(max_length=245)


# class post(models.Model):
#     student_id = models.IntegerField(blank=True, unique=True)
    

# def save(self, *args, **kwargs):
#     global random_slug
#         random_slug = slugify(self.first_name + self.last_name + generate_random_id())

#         while CustomUser.objects.filter(slug=random_slug).exists():
#             random_slug = slugify(self.first_name + self.last_name + generate_random_id())

#         self.slug = random_slug
    
# super().save(*args, **kwargs)


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


    


