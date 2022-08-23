from cmath import inf
from functools import partial
from rest_framework.response import Response
from rest_framework.decorators import api_view
from elevator.models import Elevator
from .serializers import ElevatorSerializer
import time
from elevator.scripts import optimal



# @api_view(['GET'])
# def initialise(request):
#     for i in range(0,5):
#         Elevator.objects.create(floor=0, direction='Up', doorStatus='C', motion='S', operational=True)
#     serializer = ElevatorSerializer(Elevator.objects.all(), many=True)
#     return Response({"message": serializer.data})

"""
1.
Initialises five elevators with default values.
/initialise
object:
{
"elevators":5
}
"""

@api_view(['POST'])
def initialise(request):

    n = request.data['elevators']
    print(n)
    
    for i in range(0,n):
        Elevator.objects.create(floor=0, doorStatus='Closed', motion='Stopped', operational=True)
    serializer = ElevatorSerializer(Elevator.objects.all(), many=True)
    
    return Response({"message": serializer.data})

    
# https://stackoverflow.com/questions/3805958/how-to-delete-a-record-in-django-models
"""
2. List of requests for elevators.
Post and Get
/direction
object:
{
    "listofRequest":"[1,8,10,4,6]"
}

"""

@api_view(['POST','GET'])
def lorequest(request,pk):
    elevator = Elevator.objects.get(id=pk)
    if request.method == 'POST':
        serializer = ElevatorSerializer(instance=elevator, data=request.data,partial=True)# set partial=True to update a data partially
        if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
        return Response(data="wrong parameters")
    else:
        serializer = ElevatorSerializer(instance=elevator)

        if serializer.data['operational'] == True:
            elevator = Elevator.objects.get(id=pk)
            listofRequest = serializer.data['listofRequest']
            return Response(data=listofRequest)
        else:
            return Response(data="Elevator is not operational")


    

"""
3. Get  Next Destination Floor.
/nextfloor

"""

@api_view(['GET'])
def nextfloor(request,pk):
    elevator = Elevator.objects.get(id=pk)
    serializer = ElevatorSerializer(instance=elevator)
    operational = serializer.data['operational']
    listofRequest = serializer.data['listofRequest']
    listofRequest = listofRequest[1:-1].split(',')
    li = list(listofRequest)
    if operational == True:
        return Response(data=li[0])
    else:
        return Response(data="Elevator is not operational")

"""
4. Get Direction Up or down?.
/direction
object:

"""

@api_view(['GET'])
def direction(request,pk):
    elevator = Elevator.objects.get(id=pk)
    serializer = ElevatorSerializer(instance=elevator)
    currentFloor = serializer.data['currentFloor']
    listofRequest = serializer.data['listofRequest']
    listofRequest = listofRequest[1:-1].split(',')
    li = list(listofRequest)
    if serializer.data['operational'] == True:
        if(int(li[0]) > currentFloor):
            return Response(data='Up')
        elif (int(li[0]) < currentFloor):
            return Response(data='Down')
        else :
            Elevator.objects.filter(id=pk).update(motion="Stopped")
            return Response(data='Reached Floor')
    else:
        return Response(data="Elevator is not operational")
    

"""
5. Get and Post Status of Elevator (maintanence or operational).
/status
object:
{
    "operational":true
}
"""

@api_view(['GET','POST'])

def status(request,pk):
    elevator = Elevator.objects.get(id=pk)
    if request.method == 'POST':
        serializer = ElevatorSerializer(instance=elevator, data=request.data,partial=True)# set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data="wrong parameters")
    else:
        elevator = Elevator.objects.get(id=pk)
        serializer = ElevatorSerializer(instance=elevator)
        operational = serializer.data['operational']
        if operational == True:
            return Response(data="Elevator is operational")
        else:
            return Response(data="Elevator is not operational")


"""
6. Get and Post Status of Door (open or closed).
/door
object:
{
    "doorStatus":"Open"
}
"""

@api_view(['GET','POST'])

def door(request,pk):
    elevator = Elevator.objects.get(id=pk)
    if request.method == 'POST':
        serializer = ElevatorSerializer(instance=elevator, data=request.data,partial=True)# set partial=True to update a data partially
        if serializer.data["motion"] == "Stopped":
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
        elif serializer.data["motion"] == "Moving" and serializer.data["doorStatus"] == "Closed":
            return Response(data="Elevator is moving cannot open ")
    else:
        elevator = Elevator.objects.get(id=pk)
        serializer = ElevatorSerializer(instance=elevator)
        status = serializer.data['doorStatus']
        return Response(data=status)

"""
7. Get Optimal Elevator id.
/optimal
object:
{
    "buttonPressFloor":5
}
return 
{
    "person":[5,2,6,1,8] persons on which floor
}
"""
@api_view(['POST'])
def liftAssigner(request):
    q = request.data["person"]
    ans = []
    for i in q:
        ans.append(optimal(i))

    print(ans)
    return Response(data=ans)


    

"""
8. Get busy/Active Elevator id by motion.
/active

"""

@api_view(['GET'])
def active(request,pk):
    elevator = Elevator.objects.get(id=pk)
    serializer = ElevatorSerializer(instance=elevator)
    motion = serializer.data['motion']
    print(motion)
    if motion == 'Stopped':
        return Response(data="active")
    elif motion == "Moving":
        return Response(data="busy")

"""
9. Get and Post Status of Motion (moving or stopped).
/motion
object:
{
  "motion":"Moving"
}
"""

@api_view(['GET','POST'])
def motion(request,pk):
    elevator = Elevator.objects.get(id=pk)
    if request.method == 'POST':
        serializer = ElevatorSerializer(instance=elevator, data=request.data,partial=True)# set partial=True to update a data partially
        if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
        return Response(data="wrong parameters")
    else:
        elevator = Elevator.objects.get(id=pk)
        serializer = ElevatorSerializer(instance=elevator)
        motion = serializer.data['motion']
        print(motion)
        if(motion == "Moving"):
            return Response(data="Moving")
        else:
            return Response(data="Stopped")


"""
10. Deinitialize Elevator.
/deinitialize
"""

@api_view(['POST'])
def deinitialise(request):

    n = request.data['deleteElevators']
    print(n)
    
    for i in range(0,n):
        Elevator.objects.delete()
    serializer = ElevatorSerializer(Elevator.objects.all(), many=True)
    
    return Response({"message": serializer.data})