from django import forms
from django.db.models.fields import AutoField

from .models import Appointment
from core.models import Doctor, Patient

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['doctor', 'speciality', 'appointment_date', 'appointment_time', 'description']


class PatientAppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['doctor', 'speciality', 'appointment_date', 'appointment_time', 'description']
