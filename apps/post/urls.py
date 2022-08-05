from django.urls import path 
from .views import postCreateView
from .views import postListView
from .views import postDetailView
from .views import postUpdateView
from .views import postDeleteView


urlpatterns = [
    path('',postCreateView.as_view(),
    name='home'),
    path('list/', postListView.as_view()),
    path('detail/<pk>/', postDetailView.as_view()),
    path('update/<pk>/', postUpdateView.as_view()),
    path('delete/<pk>/', postDeleteView.as_view())
    ]