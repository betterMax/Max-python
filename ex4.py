# There are 100 cars
cars = 100
# Capacity of each is 4
space_in_a_car = 4.0
# There are 30 drivers at total
drivers = 30
# There are 90 passengers
passengers = 90
# The number of cars not driven is equal to the difference between cars and drivers
cars_not_driven = cars-drivers
# The number of cars driven is eual to the number of drivers
cars_driven = drivers
# The carpool capacity equals the number of cars driven multiplied by space in each car
carpool_capacity = cars_driven * space_in_a_car
# The number of average passengers in each car equals passengers dvided by cars driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
