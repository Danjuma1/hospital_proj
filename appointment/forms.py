from django import forms

from .models import Appointment
from core.models import Doctor, Patient

class AppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=Patient.objects.all(), empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model=Appointment
        fields=['description', 'appointmentDate']


class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model=Appointment
        fields=['description', 'appointmentDate']