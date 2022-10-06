from django.contrib import admin
from .models import *


class PatientAdmin(admin.ModelAdmin):
   list_display = ('first_name', 'last_name', 'age','address','gender')
   search_fields = ('first_name', 'last_name')
admin.site.register(Patient, PatientAdmin)


class ReminderAdmin(admin.ModelAdmin):
   list_display = ('recipient', 'message', 'reminder_status', 'date')
   search_fields = ('customer', 'date')
admin.site.register(Reminder, ReminderAdmin)


class MedicineInformationAdmin(admin.ModelAdmin):
   list_display = ('medicine_name', 'reminder_time',
                   'frequency', 'reminder_time',)
   search_fields = ('patient', 'reminder_time',)
admin.site.register(MedicineInformation, MedicineInformationAdmin)


class ImageVerificationAdmin(admin.ModelAdmin):
   list_display = ('image_id', 'verified_image', 'date',)
   search_fields = ('image_id', 'date',)
admin.site.register(ImageVerification, ImageVerificationAdmin)
