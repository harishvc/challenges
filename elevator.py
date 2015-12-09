'''
Design Elevator system using Object Oriented Programming Concepts

OO Concepts:
1. Encapsulation: Binding code and data it manipulates and keeping it safe from misuse. Variables here are private
2. Polymorphism: Many forms in Greek. Using an operator or function in different ways for different data input. 
3. Inheritance: One object acquires properties of another object
'''


class Elevator:
    def __init__(self):
        self.__max_capacity = 200
        self.__location= "ABCD Inc"
        self.__support = "18001234567"
        
class MyElevator:
    def __init__(self,name,tfloors,cfloor,dfloor):
        self.name = name  #Identifier
        Elevator.__init__(self)
        self.__Tfloor = tfloors  #total #floors the elevator serves
        self.__Cfloor = cfloor   #current floor the elevator is at
        self.__Dfloor = dfloor   #destination floor
    #def __del__(self):
        #print("destructor invoked")
    def status(self):
        return("Elevator Name:" + self.name +" Floor:"+str(self.__Cfloor) + " Destination:" + str(self.__Dfloor))
    def floor(self):
        return self.__Cfloor
    def goUp(self,x=1):
        assert self.__Cfloor + x <= self.__Tfloor, "error"
        self.__Cfloor += x
        self.__capacity = capacity
    def goDown(self,x=1):
        assert self.__Cfloor - x >= 1, "error"
        self.__Cfloor -= x
        self.__capacity = capacity
    def flightPath(self,serviceFloor):
        if (self.__Cfloor <= self.__Dfloor):
            t1 = [x for x in range(self.__Cfloor,self.__Dfloor+1)]
            try:
                #on way to destination
                c1 = t1.index(serviceFloor)
            except:
                #floors from destination to next service request
                c1 = abs(self.__Dfloor - serviceFloor)
        else:
            t1 = [x for x in reversed(range(self.__Dfloor,self.__Cfloor+1))]
            try:
                #on way to destination
                c1 = t1.index(serviceFloor)
            except:
                #floors from destination to next service request
                c1 = abs(self.__Dfloor - serviceFloor)
        return c1
            
#Detrmine which elevator will service the request
def NextElevator(A,B,serviceFloor):
    path1 = A.flightPath(serviceFloor)
    path2 = B.flightPath(serviceFloor)
    #Senario 1: path exisits
    if(path1 > 0 and path1 <= path2):
        print ("Elevator A on the way")
    else:
        print ("Elevator B on the way")
    return
    
    
A = MyElevator("A",25,2,15)
B = MyElevator("B",20,5,17)
print("Elevator Status:")
print(A.status())
print(B.status())
#Customer pushes elevator button on floor 15
print("Customer waiting on floor 20 ...")
NextElevator(A,B,20)