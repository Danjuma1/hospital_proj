from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group

from . import forms, models

# Home view
def home_view(request):
    return render(request, 'core/index.html')

# Doctor signup view
def doctor_signup_view(request):
    userForm = forms.DoctorUserForm()
    doctorForm = forms.DoctorForm()
    mydict = {'userForm':userForm, 'doctorForm':doctorForm}
    if request.method == 'POST':
        userForm = forms.DoctorUserForm(request.POST)
        doctorForm = forms.DoctorForm(request.POST, request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            doctor = doctorForm.save()
            doctor.user = user
            doctor = doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)
        return HttpResponseRedirect('doctor-login')
    return render(request, 'core/doctorsignup.html', context=mydict)

# Patient signup view
def patient_signup_view(request):
    userForm = forms.PatientUserForm()
    patientForm = forms.PatientForm()
    mydict = {'userForm':userForm, 'patientForm':patientForm}
    if request.method == 'POST':
        userForm = forms.PatientUserForm(request.POST)
        patientForm = forms.PatientForm(request.POST, request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            patient = patientForm.save()
            patient.user = user
            patient = patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patient-login')
    return render(request, 'core/patientsignup.html', context=mydict)


# Check if user is doctor or patient upon login to return respective dashboard
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

def afterlogin_view(request):
    if is_doctor(request.user):
            return redirect('doctor-dashboard')
    elif is_patient(request.user):
            return redirect('patient-dashboard')


# Dashboards
def doctor_dashboard_view(request):
    return render(request, 'core/doctor_dashboard.html')

def patient_dashboard_view(request):
    return render(request, 'core/patient_dashboard.html')
