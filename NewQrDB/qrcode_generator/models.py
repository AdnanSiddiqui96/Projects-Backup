# qrcode_generator/models.py

from django.db import models

class QRCode(models.Model):
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='qrcodes')
    created_at = models.DateTimeField(auto_now_add=True)
