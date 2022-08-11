from django.shortcuts import render, redirect
from .models import Post
# from .utils import generate_random_id
from django.contrib.auth import get_user_model
import math, random
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