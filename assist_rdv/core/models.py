from django.db import models



class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    client_name = models.CharField(max_length=200)
    client_phone = models.CharField(max_length=15)
    client_email = models.EmailField()
    client_note = models.TextField(max_length=900)
    



# Create your models here.
