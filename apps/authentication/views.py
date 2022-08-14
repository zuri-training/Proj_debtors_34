from django.shortcuts import render, redirect
from django.http import HttpResponse
import math, random
from .models import SchoolModel, CustomSchoolUser
from django.contrib.auth.base_user import BaseUserManager
from .forms import EditProfileForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import views as auth_views
from apps.post.models import Post
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib.auth.views import PasswordChangeView
import sendgrid
from sendgrid.helpers.mail import *
from my_debtors.settings import SENDGRID_API_KEY

# Create your views here.

# ****************** OTP *******************************

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
    email = request.POST['email'].lower()

    o=generateOTP()

    message = Mail(
            from_email='Project.debtors@gmail.com',
            to_emails=[email],
            subject='Sending with Twilio SendGrid is Fun',    
            html_content='<strong>Yoour OTP is </strong>' + o)
    try:
        sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)

        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

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
        # print(password)
        # zL9PcJFffq blueivy
        # feraRh4NgN greeengarden
        # d4P3v6jRXj johndoe
        email = school.email
        new_school_user = CustomSchoolUser.objects.create_user(email=email, password=password, first_name=school.administrator_name, last_name=school.school_name)
        new_school_user.save()
        return redirect("reg_success")
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

def DashboardView(request):
    posts = Post.objects.all()

    return render(request, 'authentication/dashboard.html', {'posts': posts})

class EditProfileView(FormView):
    template_name = 'authentication/settings1.html'

    def get_context_data(self, **kwargs):
        context = super(UserEditView, self).get_context_data(**kwargs)

        context['edit_profile_form'] = EditProfileForm(prefix='EditProfileForm')
        context['edit_password_form'] = PasswordChangeForm(prefix='PasswordChangeForm')
        return context


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'authentication/settings1.html'
    success_url = reverse_lazy('success')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('homepage')


def search_students(request):
    if request.method == "POST":
        searched = request.POST['searched']    
        students = Post.objects.filter(name__contains=searched)
        return render(request, "authentication/search_students.html", {'searched':searched, 'students':students})

    else:
        return render(request, "authentication/search_students.html", {})
