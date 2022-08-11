from django.urls import path
from . import views

urlpatterns = [
    path('add-debtor/', views.AddDebtorView, name='add-debtor')
]