from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('edit', views.edit, name='edit'),    
    path('how', views.how, name='how'),    
    path('cont', views.cont, name='cont'),    
]
