from django.contrib import admin
from Vt.ear_health_professional.models import *
# Register your models here.

admin.site.register(Doctor_Speciality)
admin.site.register(Field_Speciality)
admin.site.register(Schecule)
 
admin.site.register(Group)
admin.site.register(Contact)
admin.site.register(Avalibility)
admin.site.register(Hospital)
admin.site.register(Admin_Account)
admin.site.register(Super_AdminAccount)
admin.site.register(Packages)
admin.site.register(HospitalAccount)
admin.site.register(Clinics_Branch)
admin.site.register(Hospital_Speciality)
admin.site.register(Rating_Review)
admin.site.register(Doctor_Package)
admin.site.register(Doctor_Subscription)



# admin.site.register(Health_Professional_Account)
@admin.register(Health_Professional_Account)
class doctordata(admin.ModelAdmin):
    list_display = ("Health_Professional_Id", "Username","Email")
    
    search_fields = ("Health_Professional_Id", "Username","Email")