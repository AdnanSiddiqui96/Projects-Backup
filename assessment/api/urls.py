from .views import *
from django.urls import path

urlpatterns = [
    path('signup', signups.as_view()),
    path('login', login.as_view()),   
    path('apply', applyloan.as_view()),   
    path('status', loanstatus.as_view()),   
    path('loanstatus', loanblock.as_view()),   
       
]