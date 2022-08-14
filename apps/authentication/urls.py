from django.urls import path
from . import views

urlpatterns = [
    path('success', views.reg_success, name='reg_success'),
    path('register/', views.verify, name="register"),
    path('waiting_view/', views.waiting_view, name='waiting_view'),
    path("send_otp",views.send_otp,name="send otp"),
    path('login/', views.LoginView.as_view() ,name="logins"),
    path('student-contend/', views.StudentContend, name="StudentContend"),
    path('dashboard/', views.DashboardView, name="dashboard"),
    path('search_students/', views.search_students, name="search_students"),
    path('settings/', views.UserEditView.as_view(), name="settings"),
    path('edit-password/', views.PasswordsChangeView.as_view(template_name='authentication/edit_password.html'), name="edit_password"),
]