"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),

    path('doctor-signup', views.doctor_signup_view, name='doctor-signup'),
    path('patient-signup', views.patient_signup_view, name='patient-signup'),

    path('login', LoginView.as_view(template_name='core/login.html'), name='login'),
    # path('patient-login', LoginView.as_view(template_name='core/patientlogin.html'), name='patient-login'),

    # path('afterlogin', views.afterlogin_view,name='afterlogin'),
    
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),

    path('dashboard', views.dashboard_view, name='dashboard'),
    # path('patient-dashboard', views.patient_dashboard_view, name='patient-dashboard'),

]
