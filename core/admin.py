from django.contrib import admin
from .models import Doctor, Patient

class DoctorAdmin(admin.ModelAdmin):
    pass

class PatientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
