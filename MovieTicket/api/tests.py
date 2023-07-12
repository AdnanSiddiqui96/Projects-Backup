from django.test import TestCase
from api .models import *

# Create your tests here.


# Bulk Movie insertion
# def post(self, request):
#     movie_list = request.data.get('movies')  # Assuming 'movies' is a list of movie data

#     movie_objects = []
#     for movie_data in movie_list:
#         title = movie_data.get('title')
#         description = movie_data.get('description')
#         genre = movie_data.get('genre')
#         duration = movie_data.get('duration')
#         poster = movie_data.get('poster')

#         movie_object = Movie(
#             title=title,
#             description=description,
#             genre=genre,
#             duration=duration,
#             poster=poster
#         )
#         movie_objects.append(movie_object)

#     Movie.objects.bulk_create(movie_objects)

#     return Response({'status': True, 'message': 'Bulk insertion of movies successful'})




# [3:44 AM, 6/27/2023] HNH Adil: from datetime import timedelta, date

# Add Employee_Slot for Saloon Booking Section
# class employee_timing_slot(APIView):
#     def get(self, request):
#         uid = request.GET['uid']
#         mydata = employee_timing.objects.filter(employee_name_id__uid=uid).values('starttime','endtime').order_by("-created_at")
#         interval = employee_timing.objects.filter(employee_anyone_id__uid=uid).values('starttime','endtime').order_by("-created_at")
#         if mydata or interval:
#             time_slots = []
#             for data in mydata:
#                 start_time = datetime.combine(datetime.today(), data['starttime'])
#                 end_time = datetime.combine(datetime.today(), data['endtime'])
#                 while start_time.time() <= end_time.time():
#                         time_slots.append(start_time.strftime("%H:%M"))
#                         start_time += timedelta(minutes=30)
#             for data in interval:
#                 start_time = datetime.combine(datetime.today(), data['starttime'])
#                 end_time = datetime.combine(datetime.today(), data['endtime'])
#                 while start_time.time() <= end_time.time():
#                         time_slots.append(start_time.strftime("%H:%M"))
#                         start_time += timedelta(minutes=30)
#             return Response({"status":True ,'Time_slots':time_slots})
#         else:
#             return Response({"status":False,'msg':'No Employee available in this uid'})
# [3:44 AM, 6/27/2023] HNH Adil: class employee_timing(BaseModel):
#     starttime = models.TimeField(null=True, blank=True)
#     endtime = models.TimeField(null=True, blank=True)
#     employee_name_id = models.ForeignKey(employee_name, blank = True, null = True, on_delete = models.CASCADE)
#     employee_anyone_id = models.ForeignKey(employee_anyone, blank = True, null = True, on_delete = models.CASCADE)
#     # saloon_id = models.ForeignKey(saloon, blank = True, null = True, on_delete = models.CASCADE)

#     def _int_(self):
#         return self.starttime


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_showtime(request):
    if request.method == 'POST':
        # Parse the request body as JSON
        data = json.loads(request.body)
        
        # Extract the fields from the JSON data
        date = data.get('date')
        availableseats = data.get('availableseats')
        starttime = data.get('starttime')
        endtime = data.get('endtime')
        movie_id = data.get('movie_id')
        
        try:
            # Create a new Showtime instance
            showtime = Showtime.objects.create(
                date=date,
                availableseats=availableseats,
                starttime=starttime,
                endtime=endtime,
                movie_id=movie_id
            )
            
            # Return a JSON response with the created showtime's details
            return JsonResponse({'showtime_id': showtime.id, 'message': 'Showtime created successfully'})
        
        except Exception as e:
            # Return an error response if there's an exception
            return JsonResponse({'error': str(e)}, status=500)
    
    # Return an error response for unsupported request methods
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)



# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

@csrf_exempt
def update_showtime(request, showtime_id):
    try:
        # Retrieve the Showtime instance based on the provided showtime_id
        showtime = Showtime.objects.get(id=showtime_id)
        
        if request.method == 'PUT':
            # Parse the request body as JSON
            data = json.loads(request.body)
            
            # Update the Showtime instance with the new data
            showtime.date = data.get('date', showtime.date)
            showtime.availableseats = data.get('availableseats', showtime.availableseats)
            showtime.starttime = data.get('starttime', showtime.starttime)
            showtime.endtime = data.get('endtime', showtime.endtime)
            showtime.movie_id = data.get('movie_id', showtime.movie_id)
            
            # Save the updated Showtime instance
            showtime.save()
            
            # Return a JSON response with the updated showtime's details
            return JsonResponse({'showtime_id': showtime.id, 'message': 'Showtime updated successfully'})
    
    except Showtime.DoesNotExist:
        # Return an error response if the Showtime instance is not found
        return JsonResponse({'error': 'Showtime does not exist'}, status=404)
    
    except Exception as e:
        # Return an error response if there's an exception
        return JsonResponse({'error': str(e)}, status=500)
    
    # Return an error response for unsupported request methods
    return JsonResponse({'error': 'Only PUT requests are allowed'}, status=405)
