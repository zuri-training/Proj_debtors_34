from django.urls import path
from . import views

urlpatterns = [
    path('add-debtor/', views.AddDebtorView, name='add-debtor'),
    path('feed/', views.FeedView, name='feed'),
    path('post/<int:pk>/comment/', views.AddCommentView.as_view(), name="add_comment"),
]