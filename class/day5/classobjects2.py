#make your own class
class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

#given vehicle data
car = Vehicle('Nissan', 'Leaf', 2015)

#print attributes of car
print car.make
print car.model
print car.year

