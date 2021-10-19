from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import Appointment
from core.models import Doctor, Patient
from .forms import AppointmentForm, PatientAppointmentForm

from core.views import (
    is_doctor,
    is_patient
)

@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_appointment_view(request):
    doctor = Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    return render(request,'hospital/doctor_appointment.html',{'doctor':doctor})



@login_required(login_url='doctorlogin')
@user_passes_test(is_doctor)
def doctor_view_appointment_view(request):
    doctor = Doctor.objects.get(user_id=request.user.id) #for profile picture of doctor in sidebar
    appointments = Appointment.objects.all().filter(status=True,doctorId=request.user.id)
    patientid=[]
    for a in appointments:
        patientid.append(a.patientId)
    patients = Patient.objects.all().filter(status=True,user_id__in=patientid)
    appointments = zip(appointments,patients)
    return render(request,'hospital/doctor_view_appointment.html',{'appointments':appointments,'doctor':doctor})


#  PATIENTS

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_appointment_view(request):
    patient = Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    return render(request,'hospital/patient_appointment.html',{'patient':patient})



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_book_appointment_view(request):
    appointmentForm = PatientAppointmentForm()
    patient = Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    message=None
    mydict={'appointmentForm':appointmentForm,'patient':patient,'message':message}
    if request.method=='POST':
        appointmentForm = PatientAppointmentForm(request.POST)
        if appointmentForm.is_valid():
            print(request.POST.get('doctorId'))
            desc=request.POST.get('description')

            doctor = Doctor.objects.get(user_id=request.POST.get('doctorId'))
            
            appointment=appointmentForm.save(commit=False)
            appointment.doctorId=request.POST.get('doctorId')
            appointment.patientId=request.user.id #----user can choose any patient but only their info will be stored
            appointment.doctorName = User.objects.get(id=request.POST.get('doctorId')).first_name
            appointment.patientName=request.user.first_name #----user can choose any patient but only their info will be stored
            appointment.status=False
            appointment.save()
        return HttpResponseRedirect('patient-view-appointment')
    return render(request,'appointment/patient_book_appointment.html',context=mydict)



def patient_view_doctor_view(request):
    doctors = Doctor.objects.all().filter()
    patient = Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    return render(request,'appointment/patient_view_doctor.html',{'patient':patient,'doctors':doctors})



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_view_appointment_view(request):
    patient = Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    appointments = Appointment.objects.all().filter(patientId=request.user.id)
    return render(request,'appointment/patient_view_appointment.html',{'appointments':appointments,'patient':patient})



