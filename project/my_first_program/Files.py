class vehicle:
    def __init__(self, wheels = 0, seats = 0):
        self.seats = seats
        self.wheels = wheels


class Bike(vehicle):
        def __init__(self,seats=1):
             super().__init__(2, seats)
        def turn(self):
             print("Bike turning")


class Car(vehicle):
    def __init__(self,wheels=4,seats=4):
          if wheels >= 4:
               if seats >=2:
                super().__init__(wheels, seats)
    def turn(self):
        print("Car turning")
     

def print_v(Vehicle: vehicle):
     print(f"seats: {Vehicle.seats}, Wheels: {Vehicle.wheels}")

class Horse:
     def __init__(self):pass
     def turn (self):
          print("horse turning")
     
v_list= [Car(), Car(),Bike(),Bike(),Car(),Bike(),Bike(),Car(),Bike(),Car(),Car(),Car(),Bike(),Bike(),Bike(),Horse()]
for v in v_list:
    v.turn
b= Bike(2)
c= Car()
print_v(v)