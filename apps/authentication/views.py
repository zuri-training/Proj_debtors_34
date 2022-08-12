from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from django.contrib.auth import logout
from .models import SchoolModel, CustomSchoolUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib import messages
from .forms import UserLoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import views as auth_views
from django.views.generic import ListView
from apps.post.models import Post

# Create your views here.

# from django.contrib.auth import login
# from django.shortcuts import redirect, render
# from django.urls import reverse
# from .forms import CustomUserCreationForm
        

# ****************** OTP *******************************
# def VerifyEmailView(request):
#     return render(request, 'authentication/register1.html')

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
    email = request.POST['email']
    # email.save()
    # print(email)
    o=generateOTP()
    htmlgen = '<p>Hellp, Your OTP is <strong>o</strong></p>'
    send_mail('OTP request',o,'nothing',[email], fail_silently=False, html_message=htmlgen)
    return HttpResponse(o)

# *********************** REGISTER **************************

def verify(request):
    if request.method == "POST":
        school = SchoolModel()
        school.email = request.POST.get('email')
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

        password = BaseUserManager().make_random_password()
        print(password)
        # zL9PcJFffq blueivy
        # feraRh4NgN greeengarden
        email = school.email
        new_school_user = CustomSchoolUser.objects.create_user(email=email, password=password)
        new_school_user.save()
        return redirect("reg_success")
        # return redirect("common/success.html")
    return render(request, "authentication/register1.html")

def reg_success(request):
    return render(request, "authentication/reg_success.html")

def waiting_view(request):
    return HttpResponse("Details successfully submitted, An email will be sent to you 24hours after verification of your details")

def StudentContend(request):
    return render(request, 'contend/student_contend.html')


class LoginView(auth_views.LoginView):
    template_name = 'authentication/login.html'
    success_url = reverse_lazy('dashboard')

# def LoginView(request):
#     context = {}
#     if request.method == 'POST':
#         # form = UserLoginForm(request.POST)
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         # if form.is_valid():
#         #     email = request.POST['email']
#         #     password = request.POST['password']

#         user = authenticate(email=email, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect("dashboard")
#         else:
#             messages.warning(request, 'Invalid credentials. Please try again.')

#         # else:
#         #     form = UserLoginForm()
#         #     context = {'form' : form }
#     return render(request, 'authentication/login.html', context)

# def LogoutView(request):
#     return redirect("homepage")

def DashboardView(request):
    posts = Post.objects.all()

    return render(request, 'authentication/dashboard.html', {'posts': posts})

def search_students(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        students = Post.objects.filter(name__contains=searched)
        return render(request, "authentication/search_students.html", {'searched':searched, 'students':students})

    else:
        return render(request, "authentication/search_students.html", {})
