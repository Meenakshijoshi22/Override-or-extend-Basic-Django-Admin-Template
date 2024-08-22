from django.shortcuts import render
from django.contrib.admin import site

# Create your views here.
def home(request):
   return render(request, 'home.html')

def profile_view(request):
    return render(request, 'profile.html')

def custom_admin_dashboard(request):
    return render(request, 'admin/index1.html')