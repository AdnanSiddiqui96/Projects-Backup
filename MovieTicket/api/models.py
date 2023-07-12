from django.db import models
import uuid


Role = {
    ('admin','admin'),
    ('user','user')
}




class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True ,blank=True,null=True)
    class Meta:
        abstract = True



# Create your models here.
class Account(BaseModel):
    firstname = models.CharField(max_length=255, default='')
    lastname = models.CharField(max_length=255, default='')    
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, default='')
    contact = models.CharField(max_length=255, default='')    
    role=models.CharField(choices=Role, max_length=20, default='user')

    def __str__(self):
        return self.firstname
    


class Movie(BaseModel):
    title = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')    
    genre = models.CharField(max_length=255, default='')    
    duration = models.CharField(max_length=255, default='')    
    poster = models.ImageField(upload_to='admin/',default='admin/dumm.jpg')    
    

    def __str__(self):
        return self.title
    


class Showtime(BaseModel):
    date = models.DateField()
    availableseats = models.IntegerField()
    starttime = models.TimeField(null=True, blank=True)
    endtime = models.TimeField(null=True, blank=True)   
    movei_id = models.ForeignKey(Movie, blank = True, null = True, on_delete = models.CASCADE)
    
    

    # def __str__(self):
    #     return self.movei_id
