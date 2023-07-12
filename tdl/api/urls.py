from .views import *
from django.urls import path

urlpatterns = [
    path('signup', signups.as_view()),
    path('login', login.as_view()),               
    path('dolist', task.as_view()),               
]