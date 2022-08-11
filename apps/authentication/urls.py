from django.urls import path
from . import views

urlpatterns = [
    #  path("",views.home,name="home"),
    path('success', views.reg_success, name='reg_success'),
    path('register/', views.verify, name="register"),
    path('waiting_view/', views.waiting_view, name='waiting_view'),
    path("send_otp",views.send_otp,name="send otp"),
    # path('register/otp/', views.VerifyEmailView, name="OTP"),
    path('login/', views.LoginView.as_view() ,name="logins"),
    # path('logout/', views.LogoutView, name="logout"),
    path('student-contend/', views.StudentContend, name="StudentContend"),
    path('dashboard/', views.DashboardView, name="dashboard"),
]