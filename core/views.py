from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.views import LoginView

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
            doctor = doctorForm.save(commit=False)
            doctor.user = user
            doctor.status=True
            doctor.save()
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
            patient = patientForm.save(commit=False)
            patient.user = user
            patient.status=True
            patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patient-login')
    return render(request, 'core/patientsignup.html', context=mydict)

# check if user is doctor or patient then redirect to login
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

def afterlogin_view(request):
    if is_doctor(request.user):
        return redirect('doctor-dashboard')
        
    elif is_patient(request.user):
        return redirect('patient-dashboard')
        


@login_required(login_url='doctor-login')
@user_passes_test(is_doctor)
def doctor_dashboard_view(request):
    doctor = models.Doctor.objects.get(user_id=request.user.id)
    context = {'doctor':doctor}
    return render(request,'core/doctor_dashboard.html', context)


@login_required(login_url='patient-login')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    return render(request,'core/patient_dashboard.html')


