from .views import *
from django.urls import path

urlpatterns = [
    path('signup', signups.as_view()),
    path('login', login.as_view()),        
    path('MovieManage', ManageMovie.as_view()),        
    path('Showtimes', Showtimes.as_view()),        
    path('seetsadd', addseets.as_view()),        
       
]