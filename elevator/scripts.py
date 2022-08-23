from elevator.models import Elevator
from elevator.api.serializers import ElevatorSerializer
import time
# def assignLift(persons,arr):
#     for person in persons:


def optimal(personFloor):
    
    mini = float('inf')
    index = 0
    elevator = Elevator.objects.all()
    # print(elevator)
    elevatorIndex = -100
    arr = []
    for elevator in elevator.iterator():
        serializer = ElevatorSerializer(instance=elevator)
        motion = serializer.data['motion']

        currentFloor = elevator.currentFloor
        arr.append(elevator.id)
        if(abs(currentFloor - personFloor) < mini and motion != "Moving" ):#[3,5,4,2,1] personFloor = 5
            mini = abs(currentFloor - personFloor)
            elevatorIndex  = index
        index+=1
    print(str(mini) + " diff")
    print(elevatorIndex+arr[0])
    userElevatorIndex  = elevatorIndex+arr[0]

    Elevator.objects.filter(id=userElevatorIndex).update(motion = "Moving")
    if elevatorIndex<0:
        return "All elevators are busy"
    currentUserelevator = Elevator.objects.get(id=userElevatorIndex)
    traverse(currentUserelevator.listofRequest,currentUserelevator.currentFloor,userElevatorIndex)
    return userElevatorIndex


def increment(current):
    current+=1
    time.sleep(2)
    print("Upward direction and floor number : ", current)
    
def decrement(current):
    current-=1
    time.sleep(2)
    print("Downward direction and floor number : ", current)

def traverse(lift,current,id):
    lift = lift[1:-1].split(',')
    lift = list(lift)
    print(lift)
    if lift:
        while(True):
            if lift:
                if(current > int(lift[0])):
                    decrement(current)
                    
                if(str(current) in lift):
                    print("Stop as we reached to floor number : ", current)
                    Elevator.objects.filter(id=id).update(motion = "Stopped")
                    Elevator.objects.filter(id=id).update(currentFloor = current)
                    lift.remove(str(current))
                    break
                    
                if(current < int(lift[0])):
                    increment(current)