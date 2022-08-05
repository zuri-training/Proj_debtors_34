from django.shortcuts import render

# Create your views here.

def HomeView(request):
    return render(request, "common/index.html")

def AboutView(request):
    return render(request, "common/about.html")

def FAQsView(request):
    return render(request, "common/FAQs.html")
