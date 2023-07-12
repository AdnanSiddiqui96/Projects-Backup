from django.db import models

# Create your models here.


class Databasebackup(models.Model):
    files = models.FileField(upload_to='dbbackup/',default="")
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)


        
    def __str__(self):
        return str(self.created_at)

