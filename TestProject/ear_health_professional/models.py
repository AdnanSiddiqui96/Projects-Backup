from django.db import models
from rest_framework import serializers


gender=(
    ("male","Male"),
    ("female","Female"),
)
check=(
    ("yes","YES"),
    ("no","No"),
)
Group=(
    ("public","Public"),
    ("private","Private"),
)

Days=(
    ("monday","Monday"),
    ("tuesday","Tuesday"),
     ("wednesday","Wednesday"),
    ("thursday","Thursday"),
     ("friday","Friday"),
    ("saturday","Saturday"),
     ("sunday","Sunday"),

)
status=(
    ("active","Active"),
    ("inactive","InActive"),

)
STATUS=(
    ("Available","Available"),
    ("Not_Available","Not_Available"),

)
HospitalSTATUS=(
    ('Active','Active'),
    ('Disable','Disable'),
)
Device = (

        ('ios','ios'),
        ('android','android'),
         ('web','web'),

    )



# For Super Admin


class Super_AdminAccount(models.Model):

    SId = models.AutoField(primary_key=True)
    SFname=models.CharField(max_length=100, default="First Name")
    SLname=models.CharField(max_length=100, default="Last Name")
    SEmail=models.CharField(max_length=100, default="Email Name")
    SUsername=models.CharField(max_length=100, default="Username ")
    SPassword=models.TextField(max_length=3000, default="Password ")
    SContactNo=models.CharField(max_length=100, default="Contact no")
    SProfile= models.ImageField(upload_to='SuperAdmin/',default="SuperAdmin/dummy.jpg")
    def __str__(self):
        return self.SFname

class Seradmin(serializers.ModelSerializer):
    class Meta:
        model= Super_AdminAccount
        fields=('SId','SFname','SLname','SUsername','SEmail','SContactNo','SProfile','SPassword')
    
    

class Packages(models.Model):

    PackId=models.AutoField(primary_key=True)
    PackName=models.CharField(max_length=300, default="Package Name")
    PackDescription=models.TextField(max_length=3300, default="Package Description")
    PackDoctor = models.IntegerField(default=0)
    PackHospital = models.IntegerField(default=0)
    PackDurationStart=models.DateField()
    PackDurationEnd=models.DateField()
    PackPrice= models.FloatField(default=0.0)
    Status = models.CharField(max_length=300, default="False")
    def __str__(self):
        return self.PackName

class Serpackage(serializers.ModelSerializer):
    class Meta:
        model= Packages
        fields=('PackId','PackName','PackDescription','PackDoctor','PackHospital','PackDurationStart','PackDurationEnd','PackPrice')




# Create your models here.
class HospitalAccount(models.Model):
    HospitalAccount_Id= models.AutoField(primary_key=True)
    HospitalAccount_Name=models.CharField(max_length=500, default="Hospital Name")
    HospitalAccount_Username=models.CharField(max_length=100, default="Hospital Username")
    HospitalAccount_Email=models.CharField(max_length=100, default="Hospital Email")
    HospitalAccount_Password=models.TextField(max_length=3000, default="Hospital Password")
    HospitalAccount_Address=models.CharField(max_length=100, default="Hospital Address")
    HospitalAccount_Status=models.CharField(max_length=80, choices=HospitalSTATUS , default="Disable")
    HospitalAccount_Logo = models.ImageField(upload_to="Hospital/", default="Hospital/dummy.png")
    HospitalAccount_Package=models.ForeignKey(Packages , on_delete=models.SET_NULL,blank=True,null=True)
    SuperId=models.ForeignKey(Super_AdminAccount, on_delete=models.CASCADE)
    def __str__(self):
        return self.HospitalAccount_Name
    
class SerHospitalAccount(serializers.ModelSerializer):
    package =  serializers.ReadOnlyField(source='HospitalAccount_Package.PackName')
    Hospital_Package= serializers.ReadOnlyField(source='HospitalAccount_Package.PackId')
    class Meta:
        model= HospitalAccount
        fields=('HospitalAccount_Id','Hospital_Package','HospitalAccount_Name','HospitalAccount_Username','HospitalAccount_Email','HospitalAccount_Password','HospitalAccount_Address','HospitalAccount_Status','HospitalAccount_Package','SuperId','package')

 

class Clinics_Branch(models.Model):
    Clinics_BranchId=models.AutoField(primary_key=True)
    Clinics_BranchName=models.CharField(max_length=400 , default="Branch Name")
    Clinics_BranchUsername=models.CharField(max_length=400 , default="Branch Username")
    Clinics_BranchEmail=models.CharField(max_length=400 , default="Branch Email")
    Clinics_BranchPassword=models.TextField(max_length=3000 , default="Branch Password")
    Clinics_BranchAddress=models.CharField(max_length=400 , default="Branch Address")
    Clinics_BranchCreatedDate=models.DateTimeField(auto_now_add=True, blank=True)
    HospitalAccount_Id=models.ForeignKey(HospitalAccount , on_delete=models.CASCADE)
    Mobile_Number = models.CharField(max_length=200, default="")
    OTP_Verification = models.CharField(max_length=200, default="12345")
    def __str__(self):
        return self.Clinics_BranchName

class SerClinics_Branch(serializers.ModelSerializer):
    class Meta:
        model = Clinics_Branch
        
        fields = '__all__'
        
class Admin_Account(models.Model):
    Admin_Account_id=models.AutoField(primary_key=True)
    First_Name=models.CharField(max_length=100, default="")
    Last_Name=models.CharField(max_length=100, default="")
    Email=models.EmailField(max_length=100, default="")
    Username=models.CharField(max_length=100, default="")
    Password=models.CharField(max_length=100, default="")
    Admin_Account_Image=models.ImageField(upload_to='Admin_Account/',default="Health_Professional/dummy.jpg")

    def __str__(self):
        return self.Username

class Hospital(models.Model):

    Hospital_id=models.AutoField(primary_key=True)
    Hospital_Name=models.CharField(max_length=100, default="")
    About=models.TextField(default="")
    Bio=models.TextField(default="")
    Hospital_Image=models.ImageField(upload_to='Hospital/',default="dummy.jpg")
    longitude=models.CharField(max_length=1000, default="")
    latitude=models.CharField(max_length=1000, default="")
    Status=models.CharField(max_length=100, choices=status,default="active")
    Created_at=models.DateTimeField(auto_now_add=True)
    More_Mapinfo = models.TextField(default="0")
    Hospital_Speciality = models.CharField(default="",max_length=100) 
    Location = models.CharField(default="",max_length=100) 
    HospitalAccount_Id=models.ForeignKey(HospitalAccount , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey(Clinics_Branch , on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.Hospital_Name


class Rating_Review(models.Model):

    Rating_Review_id = models.AutoField(primary_key=True)
    Hospital_Rating = models.IntegerField(default=0)
    Patient_Id=models.ForeignKey('Patient.Patient_Account' , on_delete=models.CASCADE,blank=True,null=True)
    Hospital_id=models.ForeignKey(Hospital , on_delete=models.CASCADE,blank=True,null=True)
    Hospital_Review = models.TextField(default="")


    

class Ser_Rating_Review(serializers.ModelSerializer):
    
    Patient_Name=serializers.ReadOnlyField(source="Patient_Id.Username")
    Patient_image=serializers.ReadOnlyField(source="Patient_Id.Patient_Account_Image.url")
    
    class Meta:
        model = Rating_Review
        fields = ('Patient_Name','Patient_image','Hospital_Rating','Hospital_Review')



 

# class Doctor_Package(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100, default="")
#     duraction = models.IntegerField(default=0)
#     type = models.CharField(max_length=50, default="")
#     price = models.FloatField(max_length=55, default=0)
#     status = models.BooleanField(default=False)


#     def __str__(self):
#         return self.name





class Health_Professional_Account(models.Model):
    Health_Professional_Id = models.AutoField(primary_key=True)
    Full_Name=models.TextField(default="")
    First_Name=models.CharField(max_length=100, default="")
    Last_Name=models.CharField(max_length=100, default="")
    Email=models.TextField(default="")
    Username=models.TextField(default="")
    Gender=models.CharField(max_length=100,default="")
    Date_of_Birth=models.CharField(max_length=200, default="")
    Password=models.TextField(default="")
    Degree=models.CharField(max_length=200, default="")
    Affiliation=models.CharField(max_length=200, default="")
    Bio=models.TextField(default="")
    Street_Address=models.CharField(max_length=500, default="")
    City=models.CharField(max_length=500, default="")
    State=models.CharField(max_length=500, default="")
    Country=models.CharField(max_length=500, default="")
    Location=models.CharField(max_length=500, default="")
    Role=models.CharField(max_length=100,default="Doctor")
    Status=models.CharField(max_length=100, choices=STATUS,default="Available")
    Health_Professional_Image=models.ImageField(upload_to='Health_Professional/',default="dummyprofile.jpg")
    Hospital_id=models.ForeignKey(Hospital , on_delete=models.CASCADE,blank=True,null=True)
    Mobile_Number = models.CharField(max_length=200, default="")
    Email_Verification_Code = models.CharField(max_length=200, default="")
    Email_Verification_Timestatus = models.CharField(max_length=200, default="False")
    Email_Verification_usestatus = models.CharField(max_length=200, default="False")
    OTP_Verification = models.CharField(max_length=200, default="12345")
    Doctor_rating = models.IntegerField(default=0)
    Doctor_rating_Count = models.IntegerField(default=0)
    HospitalAccount_Id=models.ForeignKey(HospitalAccount , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey(Clinics_Branch , on_delete=models.CASCADE,blank=True,null=True)
    Sender_ID = models.TextField(default="")
    Device_type = models.CharField(max_length=100,choices=Device,default="android")
    Message_Count = models.CharField(max_length=20,default="0")
    Doctor_Speciality = models.CharField(default="",max_length=100) 

  


    def __str__(self):
        return self.Full_Name

class Doctor_Package(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    duration = models.IntegerField(default=0)
    type = models.CharField(max_length=50, default="")
    price = models.FloatField(max_length=55, default=0)
    status = models.BooleanField(default=False)


    def _str_(self):
        return self.name
    

class Doctor_Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True) 
    status = models.BooleanField(default=False)
    amount = models.FloatField(max_length=55, default=0)
    doctor = models.ForeignKey(Health_Professional_Account, related_name='doctorsubscription',on_delete=models.CASCADE,blank=True,null=True)
    package = models.ForeignKey(Doctor_Package, related_name='doctorpackage',on_delete=models.CASCADE,blank=True,null=True)
    payid = models.CharField(max_length=50, default="")





class Hospital_Speciality(models.Model):
    
    Hospital_Speciality_id=models.AutoField(primary_key=True)
    Hospital_Speciality_Name=models.CharField(max_length=100, default="")
    Hospital_Speciality_Image=models.ImageField(upload_to='Hospital_Speciality/',default="dummy.jpg")
    HospitalAccount_Id=models.ForeignKey(HospitalAccount , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey(Clinics_Branch , on_delete=models.CASCADE,blank=True,null=True)
    Hospital_id=models.ForeignKey(Hospital , on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.Hospital_Speciality_Name

class Doctor_Speciality(models.Model):
    
    Speciality_id=models.AutoField(primary_key=True)
    Speciality_Name=models.CharField(max_length=100, default="")
    Health_Professional_id=models.ForeignKey(Health_Professional_Account , on_delete=models.CASCADE,blank=True,null=True)
    HospitalAccount_Id=models.ForeignKey(HospitalAccount , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey(Clinics_Branch , on_delete=models.CASCADE,blank=True,null=True)
    Hospital_id=models.ForeignKey(Hospital , on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.Speciality_Name

class Field_Speciality(models.Model):
    Field_Speciality_id=models.AutoField(primary_key=True)
    Speciality_Name=models.CharField(max_length=100, default="")
    


    def __str__(self):
        return self.Speciality_Name


##khizar

class Schecule(models.Model):
    Schecule_id=models.AutoField(primary_key=True)
    Start_Date_Range=models.DateField(blank=True, null=True)
    End_Date_Range=models.DateField(blank=True, null=True)
    Appointment_Duration=models.CharField(max_length=100, default="")
    Currency=models.CharField(max_length=100, default="")
    Price=models.CharField(max_length=100, default="")
    Health_Professional_id=models.ForeignKey(Health_Professional_Account , on_delete=models.CASCADE,blank=True,null=True)
    HospitalAccount_Id=models.ForeignKey(HospitalAccount , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey(Clinics_Branch , on_delete=models.CASCADE,blank=True,null=True)
    Monday_Duration=models.CharField(max_length=100, default="")
    Tuesday_Duration=models.CharField(max_length=100, default="")
    Wednesday_Duration=models.CharField(max_length=100, default="")
    Thursday_Duration=models.CharField(max_length=100, default="")
    Friday_Duration=models.CharField(max_length=100, default="")
    Saturday_Duration=models.CharField(max_length=100, default="")
    Sunday_Duration=models.CharField(max_length=100, default="")
    


class Avalibility(models.Model):

    Avalibility_id=models.AutoField(primary_key=True)
    Monday_From=models.TextField(default="")
    Monday_To=models.TextField(default="")
    Tuesday_From=models.TextField(default="")
    Tuesday_To=models.TextField(default="")
    Wednesday_From=models.TextField(default="")
    Wednesday_To=models.TextField(default="")
    Thursday_From=models.TextField(default="")
    Thursday_To=models.TextField(default="")
    Friday_From=models.TextField(default="")
    Friday_To=models.TextField(default="")
    Saturday_From=models.TextField(default="")
    Saturday_To=models.TextField(default="")
    Sunday_From=models.TextField(default="")
    Sunday_To=models.TextField(default="")
    Schecule_id=models.ForeignKey(Schecule , on_delete=models.CASCADE,blank=True,null=True)
    HospitalAccount_Id=models.ForeignKey(HospitalAccount , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey(Clinics_Branch , on_delete=models.CASCADE,blank=True,null=True)





class Group(models.Model):
    Group_id=models.AutoField(primary_key=True)
    Group_Name=models.CharField(max_length=100, default="")
    Speciality=models.TextField(default="No")
    Public_Private=models.CharField(max_length=100,choices=Group,default="Public")
    Members=models.TextField(default="")
    Color=models.CharField(max_length=100, default="")
    Health_Professional_id=models.ForeignKey(Health_Professional_Account , on_delete=models.CASCADE,blank=True,null=True)
    HospitalAccount_Id=models.ForeignKey(HospitalAccount , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey(Clinics_Branch , on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.Group_Name


class Contact(models.Model):
    Contact_id=models.AutoField(primary_key=True)
    Full_Name=models.CharField(max_length=100, default="")
    Email=models.EmailField(max_length=100, default="")
    Contact_No=models.CharField(max_length=100, default="")
    Message=models.TextField(default="")
    HospitalAccount_Id=models.ForeignKey(HospitalAccount , on_delete=models.CASCADE,blank=True,null=True)
    Clinics_BranchId=models.ForeignKey(Clinics_Branch , on_delete=models.CASCADE,blank=True,null=True)







