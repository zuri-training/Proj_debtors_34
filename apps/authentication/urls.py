from django.urls import path
from . import views

urlpatterns = [
    path('', views.verify, name="verify"),
    path('waiting_view/', views.waiting_view, name='waiting_view')
]