
elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1
doorID = 1

#************************************************here we create the Column*************************************************
class Column:
    def __init__(self, _id, _amountOfFloors, _amountOfElevators):
        self.ID = _id
        self.amountOfFloors = _amountOfFloors
        self.amountOfElevators = _amountOfElevators
        self.status = "online"
        self.elevatorList = []
        self.callButtonList = []
        self.createElevators()
        self.createCallButtons()

#*********************************this method creates the elevators in a list************************************
    def createElevators(self):
        global elevatorID
        for elevator in range(0, self.amountOfElevators)  :
            elevator = Elevator(elevatorID, self.amountOfFloors)
            self.elevatorList.append(elevator)
            elevatorID += 1
            
#****************************** this method is used to create the buttons outside the elevator********************
    def createCallButtons(self):
        buttonFloor = 0
        global callButtonID
        for callButton in range(0, self.amountOfFloors) :
            if buttonFloor < self.amountOfFloors:
                callButton = CallButton(callButtonID, self.amountOfFloors, "up")
                self.callButtonList.append(callButton)
                callButtonID += 1
                if buttonFloor > 1:
                    callButton = CallButton(callButtonID, self.amountOfFloors, "down")
                    self.callButtonList.append(callButton)
                    callButtonID += 1

            buttonFloor += 1

#*********************************this method request the elevator by first using the mthod findBestElevator***************************************** 
    def requestElevator(self, floor, direction):
        elevator = self.findElevator(floor, direction)
        elevator.floorRequestList.append(floor)
        elevator.door.status = "close"
        elevator.move()
        elevator.door.status = "open"
        return elevator
    
#*********************************this method find the best elevator by checking wich one is the best for the situation******************************
    def findElevator(self, requestedFloor, requestedDirection):
        bestElevatorInformations = { # directory
        'bestElevator': None,
        'bestScore': 5,
        'referenceGap': 10000000
        }
        for elevator in self.elevatorList:
        
            
            if requestedFloor == elevator.currentFloor and elevator.status == "stopped" and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(1, elevator, bestElevatorInformations, requestedFloor)
            elif requestedFloor > elevator.currentFloor and elevator.direction == "up" and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)
            elif requestedFloor < elevator.currentFloor and elevator.direction == "down" and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)
            elif elevator.status == "idle":
                bestElevatorInformations = self.checkIfElevatorIsBetter(3, elevator, bestElevatorInformations, requestedFloor)
            
            else:
                bestElevatorInformations = self.checkIfElevatorIsBetter(4, elevator, bestElevatorInformations, requestedFloor)

            
        return bestElevatorInformations['bestElevator']
    
#****************************this method creates a score system to always return the best elevator**************************
    def checkIfElevatorIsBetter(self, scoreToCheck, newElevator, bestElevatorInformations, floor):
        if (scoreToCheck < bestElevatorInformations['bestScore']):
            bestElevatorInformations['bestScore'] = scoreToCheck
            bestElevatorInformations['bestElevator'] = newElevator
            bestElevatorInformations['referenceGap']= abs(newElevator.currentFloor - floor)
        elif (bestElevatorInformations['bestScore'] == scoreToCheck):
            gap = abs(newElevator.currentFloor - floor)
            if (bestElevatorInformations['referenceGap'] > gap):
                bestElevatorInformations['bestElevator'] = newElevator
                bestElevatorInformations['referenceGap'] = gap
                bestElevatorInformations['bestScore'] = scoreToCheck

        print(bestElevatorInformations)
        return bestElevatorInformations


#***********************the elevator class creates elevator objects********************************************************
class Elevator:
    def __init__(self, _id, _amountOfFloors):
        global doorID
        self.ID = _id
        self.status = "idle"
        self.amountOfFloors = _amountOfFloors
        self.currentFloor = 1
        self.direction = None
        self.door = Door(doorID)
        doorID += 1
        self.floorRequestButtonList = []
        self.floorRequestList = []
        self.createFloorRequestButtons(self.amountOfFloors)

#************************************this method create the buttons inside the elevator**************************************
    def createFloorRequestButtons(self, _amountOfFloors):
        global floorRequestButtonID
        buttonFloor = 1
        for floorRequestButton in range(0, self.amountOfFloors):  
            floorRequestButton = FloorRequestButton(floorRequestButtonID, "off")
            floorRequestButtonID += 1
            buttonFloor += 1
            self.floorRequestButtonList.append(floorRequestButton)
        
#********************************this method request the desired floor from the user*****************************************
    def requestFloor(self,  floor):
        self.floorRequestList.append(floor)
        self.door.status = "closed"
        self.move()
        self.door.status = "open"

#***************************************the move method basically move the elevator to the desired floor**********************
    def move(self):
        while  self.floorRequestList != [] :
            destination = self.floorRequestList.pop()
            self.status = "moving"
            if self.currentFloor < destination:
                self.direction = "up"
                self.sortFloorList()
                while self.currentFloor < destination:
                    self.currentFloor += 1


            elif self.currentFloor > destination:
                self.direction = "down"
                self.sortFloorList()
                while self.currentFloor > destination:
                    self.currentFloor -= 1
                



        self.status = "stopped"
        self.status = "idle"


#**************************************this method sorts the list of request made by the user*********************************
    def sortFloorList(self):
        if self.direction == "up":
            self.floorRequestList.sort()
        else:
            self.floorRequestList.reverse()

#***************************************this class creates the callButton objects*********************************************
class CallButton:
    def __init__(self, _id, _floor, _direction):
        self.ID = _id
        self.status = "off"
        self.floor = _floor
        self.direction = _direction

#*************************************** this class here creates objects for the buttons inside the elevator****************** 
class FloorRequestButton:
    def __init__(self, _id, _floor):
        self.ID = _id
        self.status = "off"
        self.floor = _floor

#*****************************************finally this class creates door objects*********************************************
class Door:
    def __init__(self, _id):
        self.ID = _id
        self.status = "close"

