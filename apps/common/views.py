from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

# Create your views here.

def AboutView(request):
    return render(request, "common/about.html")
    def ContactView(request):
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


    form = ContactForm()
    context = {'form': form}
    return render(request, 'common/contact.html', context)

