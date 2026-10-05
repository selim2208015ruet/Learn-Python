class Car:
    def move(self):
        print("Car is moving")
    
class Boat:
    def move(self):
        print ("Boat is moving")
    
car = Car()
boat = Boat()

animals = [boat, car]

for animal in animals:
    animal.move()