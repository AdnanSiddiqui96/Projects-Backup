from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api .models import *
import api.usable as uc
from passlib.hash import django_pbkdf2_sha256 as handler
from django.db.models import F
import datetime 
import jwt
from decouple import config




# Create your views here.
#REGISTRATION API::::::
class signups(APIView):    
    def get(self,request):        
            # data = Account.objects.values(Name=F('firstname'),Email=F('email'), Role=F('role'))
            data = Account.objects.values(Name=F('firstname'),Email=F('email'), Role=F('role'))
            return Response({'status': True, 'data': data})
        

    
    def post(self, request):        
            firstname = request.data.get('firstname')
            lastname = request.data.get('lastname')
            email = request.data.get('email')
            password = request.data.get('password')
            contact = request.data.get('contact')                                            
            role = request.data.get('role')                                            
            myemail = uc.check(email)
            if uc.check(email):
                data = Account(firstname=firstname,lastname = lastname, password= handler.hash(password), email=email, contact=contact,role = role)
                data.save()
                return Response({'status': True, 'message': 'A new user added successfully'})
            else:
                return Response({'status': False, 'message': 'Invalid Email'}, status = 422)
            



class login(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')        
        fetchaccount = Account.objects.filter(email=email).first()        
        if fetchaccount is not None:
            if handler.verify(password, fetchaccount.password):
                access_token_payload = {
                    'id': str(fetchaccount.uid),
                    'Name': fetchaccount.firstname,                    
                    'Role': fetchaccount.role,                    
                }                
                if fetchaccount.role == 'admin':
                    access_token = jwt.encode(access_token_payload, config('adminkey'), algorithm='HS256')
                elif fetchaccount.role == 'user':
                    access_token = jwt.encode(access_token_payload, config('userkey'), algorithm='HS256')
                else:
                    return Response({"status": False, "message": "Invalid account role"})                                               
                return Response({
                    "status": True,
                    "message": "Login Successful",
                    "token": access_token,
                    "data": access_token_payload
                }) 
            else:
                return Response({"status": False, "message": "Invalid credentials"})
        else:
            return Response({"status": False, "message": "Account not found"})


class task(APIView):
     def get(self,request):
        data = TodoItem.objects.values()
        return Response({"status":True,"data":data})
     
     def post(self, request):        
        title = request.data.get('title')
        description = request.data.get('description')
        data = TodoItem(title=title,description = description )
        data.save()
        return Response({'status': True, 'message': 'A new task added successfully'})     
          
     def put(self,request):          
        id = request.data.get('id')                       
        title = request.data.get('title')            
        description = request.data.get('description')            
        Status = request.data.get('Status')            
        data = TodoItem.objects.filter(id = id).first()
        data.title = title
        data.description = description            
        data.status = Status
                    
        data.save()
        return Response({'status':True,'message':"Task updated successfully"})       

     def delete(self, request):
        try:
            id = request.GET['id']               
            
            data = TodoItem.objects.filter(id = id)
            if data:
                data.delete()
                return Response({'status':True,'message':"To do Item deleted successfully"})
            else:
                return Response({'status':False,'message':"Data not found"})
        except TodoItem.DoesNotExist:
            return Response({'status':False,'message':'Not Found'})


                
                


 
 

