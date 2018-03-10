# Whoops, I was supposed to begin here.
cars = 100
# this tells me the number of cars
space_in_a_car = 4.0
# this tells me how many spaces are in each car
drivers = 30
# this tells me how many drivers there are in total
passengers = 90
# this tells me the total number of passengers
cars_not_driven = cars - drivers
# this tells me how to calculate the number of cars that aren't being driven.
cars_driven = drivers
#blah blah blah
carpool_capacity = cars_driven * space_in_a_car
# just doing this for practice son
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print 87 + 90
print 90 + 787
