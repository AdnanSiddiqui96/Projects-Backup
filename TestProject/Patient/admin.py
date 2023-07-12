from django.contrib import admin
from Vt.Patient.models import *
# Register your models here.

admin.site.register(MultipleImages)
admin.site.register(Card_detail)
admin.site.register(Billing_Details)
admin.site.register(Add_Caregiver)
admin.site.register(Patient_Recent_visit)
admin.site.register(Patient_Favorited)
admin.site.register(Messages)
admin.site.register(Insurance)
admin.site.register(Doctor_Image)
admin.site.register(General_Patient_Information)



@admin.register(Patient_Account)
class PatientAccount(admin.ModelAdmin):
    list_display = ("Patient_Account_Id","Username","Date_of_Birth","Email")

    search_fields = ("Patient_Account_Id","Username","Date_of_Birth","Email")


@admin.register(Book_Appointment)
class BookAppointment(admin.ModelAdmin):
    list_display = ("Book_Appointment_id","Date","Patient_id","Status","Accept_Reject_Status","is_Paid","Online_Payment")
    
    search_fields = ("Date","Patient_id","Status","Accept_Reject_Status")