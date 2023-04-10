from django.db import models

# Create your models here.
class Hospial(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    bloodbankavailable = models.BooleanField()
    no_of_beds = models.IntegerField(default=0)
    ambulace = models.BooleanField(default=False)
    
    
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)
    def __str__(self):
       return self.name

class Patient(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Patient.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Patient.objects.filter(email = self.email):
            return True
        return  False

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
       return self.doctorname+"--"+self.patient.name;

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.id
