# qrcode_generator/urls.py

from django.urls import path
from .views import generate_qrcode

urlpatterns = [
    path('generate_qrcode/', generate_qrcode),
]
