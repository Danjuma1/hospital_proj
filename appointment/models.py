from django.db import models
from django.contrib.auth.models import User
from core.models import Doctor, Patient

class Appointment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=50, null=True)
    appointment_date = models.CharField(max_length=20, null=True)
    appointment_time = models.CharField(max_length=10, null=True)
    description = models.TextField(max_length=500, null=True)
    created_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.appointment_date
    
    
