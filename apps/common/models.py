from django.db import models

# Create your models here.
class ContactModel(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=50, default="Website Inquiry")
    message = models.TextField()

    def __str__(self):
        return self.email