from django.db import models
from rest_framework import serializers

gender=(
    ("male","Male"),
    ("female","Female"),
)
status=(
    ("Done","Done"),
    ("Pending","Pending"),
)
Data=(
    ("share_all_data","Share All Data"),
    ("share_alerts_only","Share Alerts Only"),
)
communication=(
    ("email","Email"),
    ("sms","SMS"),
)
relationship=(
    ("parent","parent"),
    ("spouse","spouse"),
    ("children","children"),
)
Device = (

        ('ios','ios'),
        ('android','android'),
         ('web','web'),

    )
 
# Create your models here.
class Patient_Account(models.Model):
    Patient_Account_Id = models.AutoField(primary_key=True)
    Full_Name=models.TextField(default="")
    First_Name=models.CharField(max_length=100, default="")
    Last_Name=models.CharField(max_length=100, default="")
    Email=models.TextField(default="")
    Username=models.TextField(default="")
    Gender=models.CharField(max_length=100, default="")
    Date_of_Birth=models.CharField(max_length=500, default="")
    Password=models.TextField(default="") 
    Street_Address=models.CharField(max_length=500, default="")
    City=models.CharField(max_length=500, default="")
    State=models.CharField(max_length=500, default="")
    Country=models.CharField(max_length=500, default="")
    Role=models.CharField(max_length=100,default="patient")
    Patient_Account_Image=models.ImageField(upload_to='Patient/',default="dummyprofile.jpg")
    Mobile_Number = models.CharField(max_length=200, default="")
    Email_Verification_Code = models.CharField(max_length=200, default="")
    Email_Verification_Timestatus = models.CharField(max_length=200, default="False")
    Email_Verification_usestatus = models.CharField(max_length=200, default="False")
    OTP_Verification = models.CharField(max_length=200, default="12345")
    ohip_number = models.TextField(default="")
    date_of_issue = models.TextField(default="")
    date_of_expiry = models.TextField(default="")
    ohip_Status = models.CharField(max_length=500, default="")
    Email_Verificatication_Status = models.CharField(max_length=500, default="False")
    Sender_ID = models.TextField(default="")
    Device_type = models.CharField(max_length=100,choices=Device,default="android")
    Message_Count = models.CharField(max_length=20,default="0")
    HospitalAccount_Id=models.ForeignKey('ear_health_professional.HospitalAccount' , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey('ear_health_professional.Clinics_Branch' , on_delete=models.CASCADE,blank=True,null=True)
    Clinic_Remove_Status = models.CharField(max_length=500, default="True")



    def __str__(self):
        return self.Full_Name





class Card_detail(models.Model):
    Card_detail_Id=models.AutoField(primary_key=True)
    Patient_id=models.ForeignKey(Patient_Account,on_delete=models.CASCADE,blank=True,null=True)
    Card_number=models.CharField(max_length=100,default="0")
    Cvc=models.IntegerField(default="12345")
    expiration_date=models.DateField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    Charge_Day=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    HospitalAccount_Id=models.ForeignKey('ear_health_professional.HospitalAccount' , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey( 'ear_health_professional.Clinics_Branch', on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.Card_number

class Billing_Details(models.Model):
    Billing_Details_id=models.AutoField(primary_key=True)
    Patient_id=models.ForeignKey(Patient_Account,on_delete=models.CASCADE,blank=True,null=True)
    Street_Address=models.TextField(default="")
    Country=models.TextField(default="")
    State=models.TextField(default="")
    City=models.TextField(default="")
    Postal_Code=models.TextField(default="")
    Email=models.TextField(default="")
    HospitalAccount_Id=models.ForeignKey('ear_health_professional.HospitalAccount' , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey( 'ear_health_professional.Clinics_Branch', on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.Country

class Insurance(models.Model):
    Insurance_id = models.AutoField(primary_key=True)
    Patient_id=models.ForeignKey(Patient_Account,on_delete=models.CASCADE,blank=True,null=True)
    insuarance_number =models.TextField(default="")
    date_of_issue = models.TextField(default="")
    date_of_expiry = models.TextField(default="")
    insurance_company_name = models.TextField(default="")
    

 

class Book_Appointment(models.Model):
 
    Book_Appointment_id= models.AutoField(primary_key=True)
    Problem=models.TextField(default="+4lISovpyV6DwPqRNcKmFvtDUyL3LLzPP9wCR3oIKMbT44gGXvC2F3EL1IvyY9MP3SmuuP5L69iN0ZJ8dJXEAQ==")
    Completion=models.TextField(default="akjMaPmdwYqc2btwftgMOLe5H1/7BQpJUJMTLVdnVZbfcEVgXZvf8W8njyEEotQF8Q1hq850qnBFDLA/FZ9c6Q==")
    Billing_Details_id=models.ForeignKey(Billing_Details,on_delete=models.CASCADE,blank=True,null=True)
    Health_Professional_id=models.ForeignKey('ear_health_professional.Health_Professional_Account',on_delete=models.CASCADE,blank=True,null=True)
    Date=models.CharField(max_length=500,default="")
    Time=models.CharField(max_length=500,default="")
    Date_of_origin=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    Patient_id=models.ForeignKey(Patient_Account,on_delete=models.CASCADE,blank=True,null=True)
    Status=models.CharField(default="Pending",max_length=20)
    Doctor_Online_Status=models.CharField(default="False",max_length=20)
    Hospital_id=models.ForeignKey('ear_health_professional.Hospital',on_delete=models.CASCADE,blank=True,null=True)
    Channel_id = models.CharField(max_length=500,default="")
    Appointment_Rating = models.IntegerField(default=0)
    HospitalAccount_Id=models.ForeignKey('ear_health_professional.HospitalAccount' , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey( 'ear_health_professional.Clinics_Branch', on_delete=models.CASCADE,blank=True,null=True)
    Cash_on_Arrival = models.CharField(max_length=500,default="False")
    Online_Payment = models.CharField(max_length=500,default="False")
    is_Paid = models.CharField(max_length=8,default="False")
    Paypal_Payment = models.CharField(max_length=500,default="False")
    Ohipe_Payment = models.CharField(max_length=500,default="False")
    Insurance_Payment = models.CharField(max_length=500,default="False")
    Accept_Reject_Status = models.CharField(max_length=500,default="Pending")
    Doctor_Slot_Timing = models.CharField(max_length=500,default="")
    Doctor_Notes = models.TextField(default="wt1lvNv9BdDP4iPKwsHoJwlWUg65Z3kIEGdEn4AZbEU/mRiiiz3TLZE5HZMCx7qWt8uJvAsH7WufJRhc+0OeeA==")
    Doctor_Prescription = models.TextField(default="wt1lvNv9BdDP4iPKwsHoJwlWUg65Z3kIEGdEn4AZbEU/mRiiiz3TLZE5HZMCx7qWt8uJvAsH7WufJRhc+0OeeA==")
    Medical_Diagnosis = models.TextField(default="yqrxWDqA9m4g/fkhdmp1jkBC1pXHyh60EwwBzdCLGGM=")
    Doctor_Read_Message = models.CharField(max_length=20,default="0")
    Patient_Read_Message = models.CharField(max_length=20,default="0")
    Patient_rating_Status = models.CharField(max_length=20,default="False")
    PDF_data = models.TextField(default="")


class General_Patient_Information(models.Model):

    General_Patient_Information_id = models.AutoField(primary_key=True)
    Book_Appointment_id=models.ForeignKey(Book_Appointment,on_delete=models.CASCADE,blank=True,null=True)
    Patient_Gender = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Patient_Name = models.TextField(default="")
    Patient_First_Name = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Patient_Last_Name = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Patient_DOB = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Patient_Height = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Patient_Weight = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Patient_Email = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Patient_reason = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")

    # Patient Medical History

    Patient_drug_allergies = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Patient_disease_list = models.TextField(default="")
    Patient_other_illness = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Patient_List_any_operations = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Patient_List_of_Current_Medications = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")

    # Healthy & Unhealthy Habits

    Exercise = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Eating_following_a_diet =models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Alcohol_Consumption = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Caffeine_Consumption = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Do_you_smoke = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")
    Medical_History = models.TextField(default="gjPDPWj20N5YisvSFYRVnzZm77L0i9YxFpf/TfngMNI=")




class Ser_Appointment(serializers.ModelSerializer):
    Patient_Name=serializers.ReadOnlyField(source="Patient_id.Username")
    Patient_Username=serializers.ReadOnlyField(source="Patient_id.Username")
    Patient_Gender=serializers.ReadOnlyField(source="Patient_id.Gender")
    Patient_Country=serializers.ReadOnlyField(source="Patient_id.Country")
    Date_of_Birth=serializers.ReadOnlyField(source="Patient_id.Date_of_Birth")
    Health_Professional_id=serializers.ReadOnlyField(source="Health_Professional_id.Health_Professional_Id")
    Health_Professional_Username=serializers.ReadOnlyField(source="Health_Professional_id.Username")
    Health_Professional_Full_Name=serializers.ReadOnlyField(source="Health_Professional_id.Full_Name")
    Hospital_id = serializers.ReadOnlyField(source="Hospital_id.Hospital_id")
    Hospital_Name = serializers.ReadOnlyField(source="Hospital_id.Hospital_Name")
    About = serializers.ReadOnlyField(source="Hospital_id.About")
    
   
    
    Status = serializers.ReadOnlyField(source="Hospital_id.Status")
    More_Mapinfo = serializers.ReadOnlyField(source="Hospital_id.More_Mapinfo")
    HospitalAccount_Id=models.ForeignKey('ear_health_professional.HospitalAccount' , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey( 'ear_health_professional.Clinics_Branch', on_delete=models.CASCADE,blank=True,null=True)
    Appointment_Status = serializers.ReadOnlyField(source = "Status")


    class Meta:
        model = Book_Appointment
        fields = ('Patient_id','Patient_Name','Patient_Username','Patient_Gender','Patient_Country','Problem','Completion','Date','Time','Date_of_origin','Status','Book_Appointment_id','Date_of_Birth','Doctor_Notes','Doctor_Prescription','Health_Professional_id','Health_Professional_Username','Health_Professional_Full_Name','Hospital_id','Hospital_Name','About','Status','More_Mapinfo','Doctor_Online_Status','Channel_id','Accept_Reject_Status','Cash_on_Arrival','Online_Payment','Ohipe_Payment','Insurance_Payment','Appointment_Status')

class Messages(models.Model):

    Messages_id = models.AutoField(primary_key=True)
    Message = models.TextField(default="")
    Book_Appointment_id=models.ForeignKey(Book_Appointment , on_delete=models.CASCADE,blank=True,null=True)
    Health_Professional_id=models.ForeignKey('ear_health_professional.Health_Professional_Account',on_delete=models.CASCADE,blank=True,null=True)
    Patient_id=models.ForeignKey(Patient_Account,on_delete=models.CASCADE,blank=True,null=True)
    Role = models.CharField(max_length=20,default="")
    Status = models.CharField(max_length=20,default="False")
    Doctor_Read_Status = models.CharField(max_length=20,default="False")
    Patient_Read_Status = models.CharField(max_length=20,default="False")
    Date = models.CharField(max_length=20,default="False")
    Time = models.CharField(max_length=20,default="False")



class SerMessage(serializers.ModelSerializer):
   
    class Meta:
        model = Messages
        fields = '__all__'



class Doctor_Image(models.Model):
    Doctor_Image_id=models.AutoField(primary_key=True)
    Book_Appointment_id=models.ForeignKey(Book_Appointment, on_delete=models.CASCADE)
    img=models.ImageField(upload_to='Appointment/',default="dummy.jpg")
    HospitalAccount_Id=models.ForeignKey('ear_health_professional.HospitalAccount' , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey( 'ear_health_professional.Clinics_Branch', on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return str(self.Doctor_Image_id)

class MultipleImages(models.Model):
    MultipleImages_id=models.AutoField(primary_key=True)
    Book_Appointment_id=models.ForeignKey(Book_Appointment, on_delete=models.CASCADE)
    img=models.ImageField(upload_to='Appointment/',default="dummy.jpg")
    HospitalAccount_Id=models.ForeignKey('ear_health_professional.HospitalAccount' , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey( 'ear_health_professional.Clinics_Branch', on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return str(self.MultipleImages_id)

class Add_Caregiver(models.Model):
    
    Add_Caregiver_id=models.AutoField(primary_key=True)
    Patient_id=models.ForeignKey(Patient_Account,on_delete=models.CASCADE,blank=True,null=True)
    Name=models.CharField(max_length=500, default="")
    Email=models.EmailField(max_length=500, default="")
    Mobile_Number=models.CharField(max_length=500, default="")
    Relationship=models.CharField(max_length=500, default="",choices=relationship)
    Data=models.CharField(max_length=500, default="",choices=Data)
    Communication=models.CharField(max_length=500, default="",choices=communication)
    HospitalAccount_Id=models.ForeignKey('ear_health_professional.HospitalAccount' , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey( 'ear_health_professional.Clinics_Branch', on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.Name


class Patient_Recent_visit(models.Model):

    Patient_Recent_visit_id = models.AutoField(primary_key=True)
    Patient_id=models.ForeignKey(Patient_Account,on_delete=models.CASCADE,blank=True,null=True)
    Health_Professional_id=models.ForeignKey('ear_health_professional.Health_Professional_Account',on_delete=models.CASCADE,blank=True,null=True)


class Patient_Favorited(models.Model):

    Patient_Favorited_id = models.AutoField(primary_key=True)
    Patient_id=models.ForeignKey(Patient_Account,on_delete=models.CASCADE,blank=True,null=True)
    Health_Professional_id=models.ForeignKey('ear_health_professional.Health_Professional_Account',on_delete=models.CASCADE,blank=True,null=True)






