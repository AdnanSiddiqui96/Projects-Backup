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
            data = Account.objects.values(Name=F('firstname'),Email=F('email'), Role=F('role'),IsBlock=F('block'))
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

class applyloan(APIView):
     def get(self,request):
        my_token=uc.userkey(request.META['HTTP_AUTHORIZATION'][7:])                          
        if my_token:        
            data = Loan.objects.filter(account_id =my_token['id']).values(Loan_Amount=F('amount'), Applied_By=F('account_id__firstname'),Status=F('status'))
            return Response({'status': True, 'data': data})
        else:
            return Response({"status":False,"Massage":"Unauthorize"})    

     def post(self, request):
        my_token = uc.userkey(request.META['HTTP_AUTHORIZATION'][7:])
        if my_token:
            checkrole = Account.objects.filter(uid=my_token['id']).first()
            if checkrole.block == False:
                amount = request.data.get('amount')
                data = Loan(amount=amount, account_id=checkrole)
                data.save()
                return Response({'status': True, 'message': 'Loan request sent successfully'})
            else:
                return Response({'status': True, 'message': "You cannot apply for a loan."})
        else:
            return Response({'status': False, 'message': 'Unauthorized'})



class loanstatus(APIView):
#Only  Admin
     def get(self,request):
        # my_token=uc.adminkey(request.META['HTTP_AUTHORIZATION'][7:])                          
        # if my_token:        
            # data = Loan.objects.values(Loan_Amount=F('amount'), Applied_By=F('account_id__firstname'),Status=F('status'))
            data = Loan.objects.values()
            return Response({'status': True, 'data': data})
        # else:
        #     return Response({"status":False,"Massage":"Unauthorize"}) 
    
#Only  Admin
     def put(self,request):  
        my_token=uc.adminkey(request.META['HTTP_AUTHORIZATION'][7:])          
        if my_token:                                           
            id = request.data.get('id')
            Status = request.data.get('Status')  
            comments = request.data.get('comments')  

            data = Loan.objects.filter(id = id).first() 
            data.id = id           
            data.status = Status 
            data.comments = comments             
            data.save()
            return Response({'status':True,'message':"Loan request updated successfully",'Record':"stloan"})
        else:
            return Response({"status":False,"Massage":"Unauthorize"}) 
        
class loanblock(APIView):
    def get(self,request): 
        # my_token=uc.adminkey(request.META['HTTP_AUTHORIZATION'][7:])          
        # if my_token:       
            # data = Account.objects.values(Name=F('firstname'),Email=F('email'), Role=F('role'))
            data = Account.objects.values(ID=F('uid'), Name=F('firstname'),Email=F('email'), Role=F('role'),IsBlock=F('block'))
            return Response({'status': True, 'data': data})
        # else:
        #     return Response({"status":False,"Massage":"Unauthorize"}) 
        

    def put(self,request):  
        # my_token=uc.adminkey(request.META['HTTP_AUTHORIZATION'][7:])          
        # if my_token:                                        
                id = request.data.get('id')
                block = request.data.get('block')  
                

                data = Account.objects.filter(uid = id).first() 
                data.uid = id           
                data.block = block 
                        
                data.save()
                return Response({'status':True,'message':"User status for Loan updated successfully",'Record':"stloan"})
        # else:
        #     return Response({"status":False,"Massage":"Unauthorize"}) 