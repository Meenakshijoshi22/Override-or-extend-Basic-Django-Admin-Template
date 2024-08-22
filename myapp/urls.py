from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('custom-admin-dashboard/', views.custom_admin_dashboard, name='custom_admin_dashboard'),
]