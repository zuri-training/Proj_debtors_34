from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='homepage'),
    path('about/', views.AboutView, name='about_us'),
    path('FAQs/', views.FAQsView, name='FAQs'),
]