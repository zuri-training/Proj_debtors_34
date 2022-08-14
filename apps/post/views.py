from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import get_user_model
import math, random
from .models import Post, Comment
from django.views.generic import CreateView
from .forms import ComentForm
from django.urls import reverse_lazy
# Create your views here.

def generate_id() :
     digits = "0123456789"
     ID = ""
     for i in range(4) :
         ID += digits[math.floor(random.random() * 10)]
     return 'STD' + ID

def AddDebtorView(request):
    if request.method == 'POST':
        debtor = Post()
        debtor.name = request.POST.get('std_name')
        debtor.Email = request.POST.get('std_email')
        debtor.Debt = request.POST.get('debt')
        debtor.phone_num = request.POST.get('std_phone_num')
        debtor.author = request.POST.get('author')
        debtor.Student_id = generate_id()

        if len(request.FILES) != 0:
            debtor.image = request.FILES['std_image']

        print(debtor.Student_id)
        debtor.save()
        return redirect("success")
    
    return render(request, 'post/adddebtor.html')

def FeedView(request):
    posts = Post.objects.all()
    return render(request, 'post/feed.html', {'posts': posts})

class AddCommentView(CreateView):
    model = Comment
    form_class = ComentForm
    template_name = 'post/feed.html'

    success_url = reverse_lazy('feed')
