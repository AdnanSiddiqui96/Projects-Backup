# qrcode_generator/views.py

from io import BytesIO
import base64
import qrcode
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import QRCode
from .serializers import QRCodeSerializer

@api_view(['POST'])
def generate_qrcode(request):
    text = request.data.get('text', '')
    
    # Generate QR code image
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save image to memory buffer
    buffer = BytesIO()
    img.save(buffer, format='JPEG')
    buffer.seek(0)
    
    # Create InMemoryUploadedFile from memory buffer
    image = InMemoryUploadedFile(buffer, None, 'qrcode.jpg', 'image/jpeg', buffer.getbuffer().nbytes, None)
    
    # Save QR code to database
    qrcode_obj = QRCode(text=text, image=image)
    qrcode_obj.save()
    
    # Serialize QR code object and return response
    serializer = QRCodeSerializer(qrcode_obj)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
