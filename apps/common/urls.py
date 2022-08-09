from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='homepage'),
    path('about/', views.AboutView, name='about_us'),
    path('FAQs/', views.FAQsView, name='FAQs'),
    path('news/', views.NewsView, name='news'),
    path('contact/', views.ContactView, name='contact'),
    path('error/', views.ErrorView, name='error'),
    path('success/', views.SuccessView, name='success'),
]