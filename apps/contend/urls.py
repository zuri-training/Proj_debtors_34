from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContendView, name='contend'),
    path('<str:room_name>/', views.RoomView, name="conversations"),
    path('checkview', views.CheckView, name="checkview"),
    path('send', views.send, name="send"),
    path('getMessages/<str:room>/', views.getMessages, name="getMessages"),
]