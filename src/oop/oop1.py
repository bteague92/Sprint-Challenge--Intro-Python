# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

## BASE CLASS
class Vehicle:
    pass

## BASE CLASS = VEHICLE
class FlightVehicle(Vehicle):
    pass
## BASE CLASS = FLIGHTVEHICLE
class Starship(FlightVehicle):
    pass
## BASE CLASS = FLIGHTVEHICLE
class Airplane(FlightVehicle):
    pass
## BASE CLASS = VEHICLE
class GroundVehicle(Vehicle):
    pass
## BASE CLASS = GROUNDVEHICLE
class Car(GroundVehicle):
    pass
## BASE CLASS = GROUNDVEHICLE
class Motorcycle(GroundVehicle):
    pass

