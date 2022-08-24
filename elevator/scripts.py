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
    elevatorIndex = -100 #if the elevatorIndex stays negative then it means no elevator is available
    arr = []
    for elevator in elevator.iterator():
        serializer = ElevatorSerializer(instance=elevator)
        print(elevator.motion)
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
        return "All elevators are busy. "
    currentUserelevator = Elevator.objects.get(id=userElevatorIndex)
    traverse(currentUserelevator.listofRequest,currentUserelevator.currentFloor,userElevatorIndex)
    return userElevatorIndex


def increment(current,id):
    current+=1
    time.sleep(2)
    Elevator.objects.filter(id=id).update(currentFloor = current)
 
    print("Upward direction and floor number: ", current)
    return current
    
def decrement(current,id):
    current-=1
    time.sleep(2)
    Elevator.objects.filter(id=id).update(currentFloor = current)
    print("Downward direction and floor number : ", current)
    return current


def traverse(lift,current,id):
    elevator = Elevator.objects.get(id=id)
    if lift:
        while(True):
            if lift:
              
                if(current >lift[0]):
                    current = decrement(current,id)
                    
                if(current == lift[0]):
                    print("Stop as we reached to floor number : ", current)
                    Elevator.objects.filter(id=id).update(motion = "Stopped")
                    lift.remove(current)
                    Elevator.objects.filter(id=id).update(listofRequest=lift) #not working
                    print(lift)
                    break
                    
                if(current < lift[0]):
                    current = increment(current,id)
                    