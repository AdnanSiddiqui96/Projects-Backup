from django.db import models
import uuid


Role = {
    ('admin','admin'),
    ('user','user')
}


Status = {
    ('complete','complete'),
    ('incomplete','incomplete')
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
  



class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status  = models.CharField(choices=Status,max_length=20,default='incomplete')

    def __str__(self):
        return self.title
