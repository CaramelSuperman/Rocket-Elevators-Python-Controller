
 columnIdCounter = 0;
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


    def createElevators():


    def createCallButtons():


    def requestElevator():

    def findElevator():

    def checkIfElevatorIsBetter():   





class Elevator:
    def __init__(self, _id, _amountOfFloors):
        self.ID = _id
        self.status = "idle"
        self.amountOfFloors = _amountOfFloors
        self.currenFloor = 1
        #self.door = new Door(+(doorID))
        self.floorRequestButtonList = []
        self.floorRequestList = []
        #self.createFloorRequestButtons(self.amountOfFloors)


    def createFloorRequestButtons():
         buttonFloor = 1 
           #for (let i = 1; i <= this.amountOfFloors; i++) {
            #let floorRequestButton = new FloorRequestButton(floorRequestButtonID++, "off", buttonFloor++)
            #this.floorRequestButtonList.push(floorRequestButton)

    def requestFloor(floor):
        self.floorRequestList.push(floor)
        self.door.status = "closed"
        #self.move()
        self.door.status = "open"


    def move():
        #while (this.floorRequestList.length != 0) {
            destination = self.floorRequestList.shift()
            self.status = "moving"
            #if (this.currentFloor < destination) {
                self.direction = "up"
                self.sortFloorList()
                #while (self.currentFloor < destination):
                    self.currentFloor++
                    self.screenDisplay = this.currentFloor
                
                 #else if (self.currentFloor > destination):
                self.direction = "down"
                self.sortFloorList()
                #while (this.currentFloor > destination):
                    #self.currentFloor--
                    #self.screenDisplay = this.currentFloor
                
            
            self.status = "stopped"
            
        
        self.status = "idle"



    def sortFloorList() :
        #if (self.direction == "up") :
            self.floorRequestList.sort()
         #else :
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
