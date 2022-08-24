from django.urls import path
from elevator.api import views 

urlpatterns = [
    path('initialise', views.initialise, name='index'),# initialises n number of objects
    path('listofrequests/<int:pk>', views.lorequest, name='lorequest'),#Get and Post List of requests for elevators
    path('nextfloor/<int:pk>', views.nextfloor, name='nextfloor'),#Get Next Destination Floor
    path('direction/<int:pk>', views.direction, name='direction'), #Get Direction Up or down?
    path('status/<int:pk>', views.status, name='status'),#Get and Post(maintanence or operational)
    path('door/<int:pk>', views.door, name='door'),#Get and Post door status manually(open or closed)
    path('liftAssigner', views.liftAssigner, name='optimal'),#Post Optimal Elevator id
    path('active/<int:pk>', views.active, name='active'),#Get busy/Active Elevator id by motion
    path('motion/<int:pk>', views.motion, name='motion'),#Get and Post Status of Motion (moving or stopped)
    path('runLift/<int:pk>', views.runLift, name='runLift'),# run the lift acc to listofRequest
    path('deinitialise', views.deinitialise, name='deinitialise'),


]
