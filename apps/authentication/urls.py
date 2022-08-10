from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #  path("",views.home,name="home"),
    path('register/', views.verify, name="register"),
    path('waiting_view/', views.waiting_view, name='waiting_view'),
    path("send_otp",views.send_otp,name="send otp"),
    path('register/otp/', views.VerifyEmailView, name="OTP"),
    # path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('student-contend/', views.StudentContend, name="StudentContend"),
    path('dashboard/', views.dashboard, name="dashboard"),
]