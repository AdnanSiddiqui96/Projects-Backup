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


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Showtime

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


    

#Movie API::::::
class ManageMovie(APIView):
    #Only Admin
    def get(self,request):
        my_token=uc.adminkey(request.META['HTTP_AUTHORIZATION'][7:])          
        if my_token:                                
            data = Movie.objects.values(ID=F('uid'),Title=F('title'),Description=F('description'),Genre=F('genre'),Duration=F('duration'))        
            return Response({'status': True, 'data': data})
        else:
            return Response({"status":False,"Massage":"Unauthorize"}) 

    #Only Admin    
    def post(self, request):
        #-----------------------------------------------------#       
        # Bulk Insertion
        # To perform bulk insertion of movie data, you can modify the post method as follows:
        # In this code, we assume that the movies field in the request data 
        # is a list of dictionaries, where each dictionary represents
        # the data for a single movie. We iterate over each movie data,
        # create a Movie object with the corresponding attributes,
        # and append it to the movie_objects list. Finally, 
        # we use the bulk_create method of the Movie model to insert 
        # all the movie objects in a single database query.
        # Please make sure that the structure of the
        # request data matches the format described above for successful bulk insertion.
        #-----------------------------------------------------#


        # movie_list = request.data.get('movies')  # Assuming 'movies' is a list of movie data
        # movie_objects = []
        # for movie_data in movie_list:
        #     title = movie_data.get('title')
        #     description = movie_data.get('description')
        #     genre = movie_data.get('genre')
        #     duration = movie_data.get('duration')
        #     poster = movie_data.get('poster')

        #     movie_object = Movie(
        #         title=title,
        #         description=description,
        #         genre=genre,
        #         duration=duration,
        #         poster=poster
        #     )
        #     movie_objects.append(movie_object)

        # Movie.objects.bulk_create(movie_objects)

        # return Response({'status': True, 'message': 'Bulk insertion of movies successful'})




            # my_token=uc.adminkey(request.META['HTTP_AUTHORIZATION'][7:])                  
            # if my_token: 
                title = request.data.get('title') 
                description = request.data.get('description') 
                genre = request.data.get('genre') 
                duration = request.data.get('duration') 
                poster = request.data.get('poster') 
                          
                data = Movie(title=title,description=description,
                genre=genre,duration=duration,poster=poster)            
                data.save()
                return Response({'status': True, 'message': 'A new Movie added successfully'})            
            # else:
            #     return Response({"status":False,"Massage":"Unauthorize"})     
            #    


    
 #Only Admin
    def put(self,request):  
        # my_token=uc.adminkey(request.META['HTTP_AUTHORIZATION'][7:])          
        # if my_token:       
            id = request.data.get('id')
            title = request.data.get('title') 
            description = request.data.get('description') 
            genre = request.data.get('genre') 
            duration = request.data.get('duration') 
            poster = request.data.get('poster') 
            data = Movie.objects.filter(uid = id).first()
            data.title =title            
            data.description =description
            data.genre =genre            
            data.duration = duration                        
            data.poster = poster     
                     
            data.save()
            return Response({'status':True,'message':"Movie updated successfully"})
        # else:
        #     return Response({"status":False,"Massage":"Unauthorize"}) 





  #Only Admin
    def delete(self,request):
        # my_token=uc.adminkey(request.META['HTTP_AUTHORIZATION'][7:])          
        # if my_token:   
            id = request.GET['id']               
            
            data = Movie.objects.filter(uid = id)
            if data:
                data.delete()
                return Response({'status':True,'message':"Movie deleted successfully"})
            else:
                return Response({'status':False,'message':"Data not found"})
        # else:
        #     return Response({"status":False,"Massage":"Unauthorize"}) 



class Showtimes(APIView):
      #Only Admin
    def get(self,request):
        # my_token=uc.adminkey(request.META['HTTP_AUTHORIZATION'][7:])          
        # if my_token:                                
            data = Showtime.objects.values(ID=F('uid'),Movie=F('movei_id__title'),From =F('starttime'),To=F('endtime'),Avaiable_Seets=F('availableseats'))        
            # data = Showtime.objects.all().values()        
            return Response({'status': True, 'data': data})
        # else:
        #     return Response({"status":False,"Massage":"Unauthorize"}) 
    def post(self, request):
        date = request.data.get('date')
        availableseats = request.data.get('availableseats')
        starttime = request.data.get('starttime')
        endtime = request.data.get('endtime')
        movei_id = request.data.get('movei_id')

        movie = Movie.objects.get(uid=movei_id)  # Retrieve the Movie instance based on movei_id

        data = Showtime(date=date, availableseats=availableseats, starttime=starttime, endtime=endtime, movei_id=movie)
        data.save()

        return Response({'status': True, 'message': 'A new Show time added successfully'})
    
    def put(self, request):
        id = request.data.get('id')
        bookseets = request.data.get('bookseets')
        movieseets = Showtime.objects.get(uid=id)

        # if not id:
        #     return Response({'status': False, 'message': 'Invalid data.'})        

        if not all([id, bookseets]):
            return Response({'status': False, 'message': 'Missing required data'})

        try:
            bookseets = int(bookseets)
            movieseets = Showtime.objects.get(uid=id).availableseats            
        except (ValueError, Showtime.DoesNotExist):
            return Response({'status': False, 'message': 'Invalid data or Movie not found'})

        if movieseets == 0:
            return Response({'status': False, 'message': 'All Seets are reserved.'})

        bookedseets = movieseets - bookseets

        data = Showtime.objects.filter(uid=id).first()
        if data:
            data.availableseats = bookedseets
            data.save()
            return Response({'status': True, 'message': "Seets are Booked successfully"})
        else:
            return Response({'status': False, 'message': "Showtime not found"})







  #Only Admin
    def delete(self,request):
        # my_token=uc.adminkey(request.META['HTTP_AUTHORIZATION'][7:])          
        # if my_token:   
            id = request.GET['id']               
            
            data = Showtime.objects.filter(uid = id)
            if data:
                data.delete()
                return Response({'status':True,'message':"Show time deleted successfully"})
            else:
                return Response({'status':False,'message':"Data not found"})
        # else:
        #     return Response({"status":False,"Massage":"Unauthorize"}) 



class addseets(APIView):
     
    def put(self,request):  
        # my_token=uc.adminkey(request.META['HTTP_AUTHORIZATION'][7:])          
        # if my_token:       
            id = request.data.get('id')                       
            availableseats = request.data.get('availableseats')            
            data = Showtime.objects.filter(uid = id).first()
            data.availableseats = availableseats            
                     
            data.save()
            return Response({'status':True,'message':"Seets of Movie updated successfully"})
        # else:
        #     return Response({"status":False,"Massage":"Unauthorize"}) 


     

class AddSeats(APIView):
     
    def put(self, request):
        endtime_to_match = '20:00:00'  # 08:00 PM
        
        try:
            # Retrieve the Showtime instance based on the provided id
            showtime_id = request.data.get('id')
            showtime = Showtime.objects.get(id=showtime_id)
            
            # Check if the endtime matches the desired value
            if showtime.endtime.strftime('%H:%M:%S') == endtime_to_match:
                # Update the availableseats to 50
                showtime.availableseats = 50
                showtime.save()
                
                return Response({'status': True, 'message': 'Seats of Movie updated successfully'})
            else:
                return Response({'status': False, 'message': 'Endtime does not match the desired value'})
        
        except Showtime.DoesNotExist:
            return Response({'status': False, 'message': 'Showtime does not exist'}, status=404)
        
        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status=500)



