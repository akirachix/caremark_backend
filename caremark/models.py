from django.db import models
from django.utils import timezone  

  
   
class Patient(models.Model):
    first_name = models.CharField(max_length=25, null=True)
    middle_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    gender_choices = (
      ('female', 'Female'),
      ('male', 'Male'),
      ('other', 'other'),
    )
    gender = models.CharField(max_length=8, null=True, choices=gender_choices)
    age = models.PositiveSmallIntegerField(null=True)
    password = models.IntegerField(null=True)
    weight = models.PositiveSmallIntegerField(default=0)
    # profile_image = models.ImageField()
    next_of_kin = models.CharField(max_length=30,null=True)
    phone_number_Next_of_kin = models.IntegerField(null=True)


class Reminder(models.Model):
    message = models.CharField(max_length=300, null=True)
    status = (('missed', 'missed'), ('seen', 'seen'), ('snooze', 'snooze'))
    recipient = models.ForeignKey(
      'Patient', on_delete=models.CASCADE, related_name='reminder_recepient')
    date = models.DateTimeField(default=timezone.now)
    appointment_date = models.DateTimeField(null=True)
    reminder_status = models.CharField(max_length=7, choices=status, null=True)


class ImageVerification(models.Model):
    image_id = models.ForeignKey(
        'Patient', on_delete=models.CASCADE, related_name='image_id_patient')
    verified_image = models.ImageField()
    reminder = models.ForeignKey(
      'reminder', on_delete=models.CASCADE, related_name='reminder_image')
    date = models.DateTimeField(default=timezone.now)
    

class MedicineInformation(models.Model):
    medicine_names_choices=()
    medicine_name = models.CharField(max_length=50, null=True)
    time = (('morning', 'morning'), ('noon', 'noon'),
          ('evening', 'evening'), ('night', 'night'))
    reminder_time = models.CharField(max_length=7, choices=time, null=True)
    frequency = models.PositiveIntegerField(null=True)
    quantity = models.PositiveIntegerField(null = True)

 