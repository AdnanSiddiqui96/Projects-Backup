from django.db import models
import uuid


Role = {
    ('admin','admin'),
    ('user','user')
}



Status = {
    ('pending','pending'),
    ('approved','approved'),
    ('rejected','rejected')
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
    email = models.EmailField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    contact = models.CharField(max_length=255, default='')
    block = models.BooleanField(default='True')#by default True not false
    role=models.CharField(choices=Role, max_length=20, default='user')

    def __str__(self):
        return self.firstname


class Loan(models.Model):    
    status = models.CharField(choices=Status, max_length=255, default='pending')
    amount = models.IntegerField(null=True, blank=True)    
    comments = models.TextField(default='')
    account_id = models.ForeignKey(Account, blank = True, null = True, on_delete = models.CASCADE)    

    def __str__(self):
        return self.status



class savetoken(models.Model): 
    access_token = models.CharField(max_length=255, default='')
    user_agent = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add='True', blank = True, null = True) 