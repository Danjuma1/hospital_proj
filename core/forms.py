from django import forms
from django.contrib.auth.models import User

from . import models

#Doctor related forms
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1', 'password2']
        # widgets = {
        # 'password': forms.PasswordInput()
        # }
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['phone','email', 'address', 'city', 'state', 'profile_pic']


#Patient related forms
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1', 'password2']
        # widgets = {
        # 'password': forms.PasswordInput()
        # }
class PatientForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['phone','email', 'address', 'city', 'state', 'profile_pic']
