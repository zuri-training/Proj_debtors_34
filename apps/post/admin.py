# from tokenize import Name
from django.contrib import admin
from.models import Name, Student_Id, Email, Debt, AmountPaid, Status

# Register your models here.

admin.site.register(Name)
admin.site.register(Student_Id)
admin.site.register(Email)
admin.site.register(Debt)
admin.site.register(AmountPaid)
admin.site.register(Status)