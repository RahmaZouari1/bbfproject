from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	
   
   path('datamodel/', views.dmtestOverview, name="dmtest-overview"),
  
]

