import jwt
from decouple import config
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
import re   
from django.contrib.auth import get_user_model, logout
from .models import *
from passlib.hash import django_pbkdf2_sha256 as handler

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
#------------------------------------------------------------------------------------------------------------

#Email Validation


def checkemailforamt(email):
    emailregix = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.match(emailregix, email)):

        return True

    else:
       return False


   
def check(mail):   
  
    if(re.search(regex,mail)):
        print("Valid Email")   
        return True   
    else:   
        return False

#------------------------------------------------------------------------------------------------------------

#Decode Token

def adminkey(token):    
    try:
        my_token=jwt.decode(token,config('adminkey'),algorithms=['HS256'])
        return my_token 
    except jwt.ExpiredSignatureError:
        return False
    except:
        return False

def userkey(token):    
    try:
        my_token=jwt.decode(token,config('userkey'),algorithms=['HS256'])
        return my_token 
    except jwt.ExpiredSignatureError:
        return False
    except:
        return False
