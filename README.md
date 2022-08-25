# REST API Simplified Elevator


The entire application Urls is within the app `elevator`.

`api` folder within app `elevator` contains the `views.py` and `serializers.py` files.

`views.py` contains the whole logic of the APIs .
`serializers.py` contains the logic to convert complex data types like queryset to json


Documentation below.

In `settings.py` in DATABASES please input your own Id and password for the database and create a database in your pgAdmin panel.

## Make a virtual enviroment
   
    Recommended python version -----> 3.9.X (The LATEST STABLE RELEASE)
    python -m venv myvenv

## Run the virtual enviroment

    myvenv\Scripts\activate.bat

## Install all dependencies

    pip install  -r requirements.txt
    
## Run the App
    
    python manage.py runserver

# REST API

The REST API to the  app is described below.

## Get list of Elevators and their Id's
   Please note the id's as they are used to send the requests

### Request

`POST /initialise`

    {
        "elevators":5
    }

### Response

    
    {
      "message": [
     {
       "id": 16,
      "doorStatus": "Closed",
      "currentFloor": 0,
      "motion": "Stopped",
      "operational": true,
      "listofRequest": null
    },
    {
      "id": 17,
      "doorStatus": "Closed",
      "currentFloor": 0,
      "motion": "Stopped",
      "operational": true,
      "listofRequest": null
    },
    {
      "id": 18,
      "doorStatus": "Closed",
      "currentFloor": 0,
      "motion": "Stopped",
      "operational": true,
      "listofRequest": null
    },
    {
      "id": 19,
      "doorStatus": "Closed",
      "currentFloor": 0,
      "motion": "Stopped",
      "operational": true,
      "listofRequest": null
    },
    {
      "id": 20,
      "doorStatus": "Closed",
      "currentFloor": 0,
      "motion": "Stopped",
      "operational": true,
      "listofRequest": null
    }

----------------------------------------------------------------------------------------------------------------------------

## List of Request
Request a floor for a particular elevetor to travel to.

### POST Request

`POST /listofrequests/:id` 

     {
         "listofRequest":4
     }
     
### Response

    { "message": "Request added"}

### GET Request

`GET /listofrequests/:id`

### Response

    [5,  8, 4]
    
-------------------------------------------------------------------------------------------------------------------------------   

## Next Destination Floor

### GET Request

`GET /nextfloor/:id`

### Response

    5
-------------------------------------------------------------------------------------------------------------------------

## Direction

### GET Request
According to the current Floor of the elevator this api will show direction

`GET /direction/:id`

### Response

    "Up"
--------------------------------------------------------------------------------------------------------------------------    

## Change Status of elevator ( operational or maintenance)

### POST Request

`POST /status/:id` 

`{
    "operational":true }`
    
### Response

    
       {
       "id": 16,
       "doorStatus": "Closed",
       "currentFloor": 0,
       "motion": "Stopped",
       "operational": false,
       "listofRequest": [
       5,
       8
       ]
       }
       

### GET Request

`GET /status/:id`

### Response

      "Elevator is operational" / "Elevator is not operational"
      
--------------------------------------------------------------------------------------------------------------------   

## Open/ Close Door

### POST Request

`POST /door/:id` 

     {
          "doorStatus":"Open"
     }

### Response

    {
    "id": 16,
    "doorStatus": "Open",
    "currentFloor": 0,
    "motion": "Stopped",
    "operational": false,
    "listofRequest": [
     5,
     8
     ]
     }

### GET Request

`GET /door/:id`

### Response

    "Open" / "Closed"
    
  --------------------------------------------------------------------------------------------------------------  
  
## Lift Assigner

### POST Request
Request of floor number is listed. The nearest elevator is selected for each request.
Both these data sets i.e request and nearest elevator are assigned in two different arrays in which each element has one 1-1 relationship

`POST /liftAsssigner` 

      {
               "person":[5,2,6,1,8]
      }
      
### Response
Returns the Id's of the elevator with respect to floor from which request originated

         [
            17,
            18,
            19,
            20,
            16
         ]
------------------------------------------------------------------------------------------------


## Elevator Busy/Active

### GET Request

`GET /active/:id`

### Response

    "active"

---------------------------------------------------------------------------------------------------

## Motion of Elevator

### POST Request

`POST /listofrequests/:id` 

      {
          "motion":"Moving"
      }
      
### Response

        {
           "id": 16,
           "doorStatus": "Open",
           "currentFloor": 0,
           "motion": "Moving",
           "operational": false,
           "listofRequest": [
                              5,
                              8
                            ]
         }

### GET Request

`GET /motion/:id`

### Response

    "Moving"/ "Stopped"
--------------------------------------------------------------------------------------------------------------------------------------------------------

## Run the elevator
   Runs the elevator with respect to the list of Requests that specific elevator has and updates currentFloor 

### GET Request

`GET /runLift/:id`

### Response

    Terminal shows the motion of the elevator and after stopping we get a response "Elevator has stopped"
    
 ---------------------------------------------------------------------------------------------------------------------------------------------------------
 
 ## List of Request

### POST Request

`GET /deinitialise/` 

### Response

    { "message": "All Elevators Deleted Please enter new number of elevators with initialise api"}


