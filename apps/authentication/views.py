import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from .models import SchoolModel, SchoolEmail, CustomSchoolUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib import messages
# Create your views here.

# from django.contrib.auth import login
# from django.shortcuts import redirect, render
# from django.urls import reverse
# from .forms import CustomUserCreationForm

# ****************** OTP *******************************
def VerifyEmailView(request):
    return render(request, 'authentication/register1.html')

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
    emails = SchoolEmail()
    emails.email = request.POST['email']
    emails.save()
    # print(email)
    o=generateOTP()
    htmlgen = '<p>Hellp, Your OTP is <strong>o</strong></p>'
    send_mail('OTP request',o,'nothing',[email], fail_silently=False, html_message=htmlgen)
    return HttpResponse(o)

# *********************** REGISTER **************************

def verify(request):
    if request.method == "POST":
        school = SchoolModel()
        emails = SchoolEmail()
        email = emails.email
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

        # email = sch_email.email
        # username = school.school_name
        password = BaseUserManager().make_random_password()

        new_school_user = CustomSchoolUser(email=email, password=password)
        new_school_user.save()
        return redirect("authentication/login.html")
        # return redirect("common/success.html")
    return render(request, "authentication/register2.html")

def waiting_view(request):
    return HttpResponse("Details successfully submitted, An email will be sent to you 24hours after verification of your details")

# def dashboard(request):
#     return render(request, "users/dashboard.html")

def StudentContend(request):
    return render(request, 'contend/student_contend.html')


def login(request):
   return render(request, 'authentication/login.html')

def dashboard(request):
    return render(request, 'authentication/dashboard.html')


