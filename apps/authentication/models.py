from django.db import models
import datetime, os
# Create your models here.

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % (timeNow,old_filename)
    return os.path.join('static/images/school_images',filename)


class SchoolModel(models.Model):
    school_name = models.CharField(max_length=200)
    administrator_name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.PositiveIntegerField()
    zip_code = models.PositiveIntegerField()
    cac_reg_number = models.PositiveIntegerField()
    school_image = models.ImageField(upload_to=filepath)
    cerificate_image = models.ImageField(upload_to=filepath)

    def __str__(self):
        return self.school_name