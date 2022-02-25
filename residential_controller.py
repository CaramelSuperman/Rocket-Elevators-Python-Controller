
elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1
doorID = 1


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

    def createElevators(self):
        global elevatorID
        for elevator in range(0, self.amountOfElevators)  :
            elevator = Elevator(elevatorID, self.amountOfFloors)
            self.elevatorList.append(elevator)
            elevatorID += 1
            

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

    def requestElevator(self, floor, direction):
        elevator = self.findElevator(floor, direction)
        elevator.floorRequestList.append(floor)
        elevator.door.status = "close"
        elevator.move()
        elevator.door.status = "open"
        return elevator

    def findElevator(self, requestedFloor, requestedDirection):
        bestElevatorInformations = {
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

    def createFloorRequestButtons(self, _amountOfFloors):
        global floorRequestButtonID
        buttonFloor = 1
        for floorRequestButton in range(0, self.amountOfFloors):  
            floorRequestButton = FloorRequestButton(floorRequestButtonID, "off")
            floorRequestButtonID += 1
            buttonFloor += 1
            self.floorRequestButtonList.append(floorRequestButton)
        

    def requestFloor(self,  floor):
        self.floorRequestList.append(floor)
        self.door.status = "closed"
        self.move()
        self.door.status = "open"

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



    def sortFloorList(self):
        if self.direction == "up":
            self.floorRequestList.sort()
        else:
            self.floorRequestList.reverse()


class CallButton:
    def __init__(self, _id, _floor, _direction):
        self.ID = _id
        self.status = "off"
        self.floor = _floor
        self.direction = _direction


class FloorRequestButton:
    def __init__(self, _id, _floor):
        self.ID = _id
        self.status = "off"
        self.floor = _floor


class Door:
    def __init__(self, _id):
        self.ID = _id
        self.status = "close"

