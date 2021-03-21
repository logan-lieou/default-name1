from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=200)
    emergency_contact = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField('birth day')
    phone = models.CharField(max_length=200, blank=True)
    alt_phone = models.CharField(max_length=200, blank=True)
    medical_plan = models.CharField(max_length=200)
    medical_id = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Record(models.Model):
    date = models.DateTimeField('date visited')
    description = models.CharField(max_length=200)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return "{0}: {1}".format(self.patient.name, self.description)


