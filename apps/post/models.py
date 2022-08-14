from webbrowser import get
from django.db import models
import uuid
from unicodedata import name
from django.db import models 
from django.contrib.auth import get_user_model
from apps.authentication.models import CustomSchoolUser

# Create your models here.

class Post(models.Model):

    STATUS_LIST = (
    ('Active', 'Active'),
    ('Pending', 'Pending'),
    ('Resolved', 'Resolved'),
    )

    name = models.CharField(max_length=45)
    Email = models.EmailField(max_length=245)
    Debt = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.IntegerField()
    AmountPaid = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    phone_num = models.IntegerField()
    image = models.ImageField()
    status = models.CharField(max_length=50, choices=STATUS_LIST, default='Active')
    Student_id = models.CharField(max_length=9, primary_key=True, editable=False)

    def __str__(self):
        return self.name + '|' + self.Student_id

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.name, self.name)
    
