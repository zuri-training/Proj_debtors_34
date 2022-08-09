from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .models import ContactModel

# Create your views here.

def HomeView(request):
    return render(request, "common/index.html")

def AboutView(request):
    return render(request, "common/about.html")

def FAQsView(request):
    return render(request, "common/FAQs.html")

def NewsView(request):
    return render(request, "common/news.html")

def ErrorView(request):
    return render(request, "common/error.html")

def SuccessView(request):
    return render(request, "common/success.html")

def ContactView(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
    if form.is_valid():
        form.save()

        subject = 'Website Inquiry'
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['email']

        try:
            send_mail(subject, message, from_email, ['Project.debtors@gmail.com'])
        except BadHeaderError:
            messages.error('Invalid header found')
        messages.success(request, 'Your message has been successfully sent')

    else:
        messages.warning(request, 'Ensure that the fields are entered and valid')
    context = {'form': form }
    return render(request, 'common/contact_us.html', context)
