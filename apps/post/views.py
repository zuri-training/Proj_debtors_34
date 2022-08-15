from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import get_user_model
import math, random
from .models import Post, Comment
from django.views.generic import CreateView
from .forms import ComentForm
from django.urls import reverse_lazy
from email.message import EmailMessage
import ssl, smtplib
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

        # print(debtor.Student_id)
        debtor.save()

        email_sender = 'nexusdomains360@gmail.com'
        email_password = 'rifbznmpwfssrpvp'
        email_reciever = debtor.Email

        subject = 'Your registraton Was Successful'
        body = 'Hi ' + debtor.name + ', you were listed as a debtor in your child/ward school on our website. If you think this is a mistake and would like to contend, please visit our website, here is your student ID with which you will contend ' + debtor.Student_id + ' You can visit our website for more inquiries. Thanks.'

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_reciever
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciever, em.as_string())

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
