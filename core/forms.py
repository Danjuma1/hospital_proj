from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . import models

#Doctor related forms
class DoctorUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields=['first_name','last_name','username', 'email', 'password1', 'password2']
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['phone', 'address', 'city', 'state', 'profile_pic']


#Patient related forms
class PatientUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields=['first_name','last_name','username', 'email', 'password1', 'password2']
        
class PatientForm(forms.ModelForm):
    class Meta:
        model=models.Patient
        fields=['phone', 'address', 'city', 'state', 'profile_pic']
