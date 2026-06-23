from django.urls import path
from . import views
app_name = 'Admin'

urlpatterns = [
    path('home/', views.home, name='home'),  
]   

