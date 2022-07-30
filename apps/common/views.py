from django.shortcuts import render

# Create your views here.

def AboutView(request):
    return render(request, "common/about.html")