#add print_info() Method

class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self.make, self.model, self.year):

#given vehicle data
car = Vehicle('Nissan', 'Leaf', 2015)

#print attributes of car
print car.make
print car.model
print car.year
print car.print_info()