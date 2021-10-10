from django.db import models
from django.contrib.auth.models import User 

# Doctor model class
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/DoctorProfilePic/', default='doctor.png')
    address = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
    
    @property
    def get_id(self):
        return self.user.id
    
    def __str__(self):
        return "Dr {} ({})".format(self.user.first_name, self.state)


# Patient model class
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/PatientProfilePic/', default='patient.png')
    address = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
    
    @property
    def get_id(self):
        return self.user.id
    
    def __str__(self):
        return self.user.first_name + ", " + self.state

