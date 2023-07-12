from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.
class Add(APIView):
    def get(self,request):
        st =  student.objects.values()
        return Response({'status':True,'Data':st})