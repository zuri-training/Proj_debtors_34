from django.shortcuts import render, redirect
from .models import SchoolModel, CustomSchoolUser
from django.http import HttpResponse
from django.contrib.auth.base_user import BaseUserManager
from django.contrib import messages
# Create your views here.

def verify(request):
    if request.method == "POST":
        school = SchoolModel()

        school.school_name = request.POST.get('name')
        school.administrator_name = request.POST.get('admin_name')
        school.address = request.POST.get('address')
        school.phone_number = request.POST.get('number')
        school.zip_code = request.POST.get('zip_code')
        school.cac_reg_number = request.POST.get('code')

        if len(request.FILES) != 0:
            school.school_image = request.FILES['photo']
            school.cerificate_image = request.FILES['certificate_img']

        school.save()
        
        
        username = school.school_name
        password = BaseUserManager().make_random_password()

        new_school_user = CustomSchoolUser(username=username, password=password)

        return redirect('waiting_view')
    return render(request, "verify.html")

def waiting_view(request):
    return HttpResponse("Details successfully submitted, An email will be sent to you 24hours after verification of your details")