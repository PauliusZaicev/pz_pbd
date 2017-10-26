# Define a class for my car
#private instance variables of a class begin with two unerscores characters
#(__colour) cannot be directly accessed

import os
os.chdir('D://DBS//5.Programming_for_big_data//Car//CA')

import unittest

#create car class (all cars must have objects from the carr class)
class Car(object):
    
    # implement the car object.
    def __init__(self, make = '', colour = '', mileage = 0, horsePower = 0, reg = ''):
        self.__colour = colour
        self.__make = make
        self.__mileage = mileage
        self.__horsePower = horsePower
        self.__reg = reg

    #get colour function
    def getColour(self):
        return self.__colour

    #get make function
    def getMake(self):
        return self.__make

    #get mileage function
    def getMileage(self):
        return self.__mileage
    #set colour fuction
    def setColour(self, colour):
        self.__colour = colour

    #set make function
    def setMake(self, make):
        self.__make = make
    #set mileage functions
    def setMileage(self, mileage):
        self.__mileage = mileage
    
    #change car colour function
    def paint(self, colour):
        self.__colour = colour
        return self.__colour
    
    #move car and update car mileage
    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage
    
    #get car horse power
    def getHorsePower(self):
        return self.__horsePower
    
    #modify horse power
    def changeHorsePower(self, horsePower):
        self.__horsePower = horsePower
        return self.__horsePower
    
    #set updated horse power
    def setHorsePower(self, horsePower):
        self.__horsePower = horsePower
    
        #get car reg
    def getReg(self):
        return self.__reg
    
    #modify horse power
    def changeReg(self, reg):
        self.__reg = reg
        return self.__reg
    
    #set updated horse power
    def setReg(self, reg):
        self.__reg = reg
     
        
    '''
    def __repr__(self):
        return 'I am a car ' + self.__horsePower'''

#set class for electric car, insert class Car as parameter
#electric class should have private variable which are only for electric car
class ElectricCar(Car):
        
    def __init__(self,reg = '', make = '', colour = '', mileage = 0, horsePower = 0, fuelCells = 1 ,   drivingHours = 0, batteries = 1):
        #call car class, car class should have all parameter which would be relevant to all cars
        Car.__init__(self, make, colour, mileage, horsePower, reg)
        #set private variable fuel cells
        self.__numberOfFuelCells = fuelCells
        #set how long electric car can drive while fully charged
        self.__drivingHours = drivingHours
        #set how many baterries vehicle has
        self.__amountOfChargebablebatteries = batteries


    #get number of cells function
    def getNumberOfFuelCells(self):
        return self.__numberOfFuelCells
    
    #set your set of cells to the new amount of cells
    def setNumberOfFuelCells(self, value):
        self.__numberOfFuelCells = value
     
    #get hours how long car can drive while fully charged 
    def getDrivingHours(self):
        return self.__drivingHours
    
    #set how long car can drive while fully charged
    def setDrivingHours (self, hours):
        self.__drivingHours = hours
        
    #get amount of baterries in vehicile 
    def getAmountOfChargebablebatteries(self):
        return self.__amountOfChargebablebatteries
    
    #set amount of baterries in vehicile
    def setAmountOfChargebablebatteries (self, batteries):
        self.__amountOfChargebablebatteries = batteries 
        
        
    #print all values as a string   
    def __repr__(self):
        #return all values which need to be sdisplayed
        return '\nRegistration No: ' + self.getReg() + ' ' +'\n\
Make: ' + self.getMake() + ' ' +'\n\
Colour: ' + self.getColour() + ' ' +'\n\
Mileage: ' + self.getMileage() + ' ' +'\n\
Horse Power: ' + self.getHorsePower() + ' ' +'\n\
Number Of Fuel Cells: ' + self.getNumberOfFuelCells() + ' ' +'\n\
Drving houts then battery charged: ' + self.getDrivingHours() + ' ' +'\n\
Amount of chargable batteries: ' + self.getAmountOfChargebablebatteries() + ' ' +'\n'

#set petrol car class, insert class car as parameter
#petrol car class should have unique privateparameters
class PetrolCar(Car):
    
    def __init__(self, reg = '', make = '', colour = '', mileage = 0, horsePower = 0, numberOfCylinders = 1, emisson = 0):
        #call car class, car class should have all required parameters for each car
        Car.__init__(self, make, colour, mileage, horsePower, reg)
        #set how many number of cylinders petrol car has
        self.__numberOfCylinders = numberOfCylinders
        self.__emission = emisson

    #function to get number of cylinders
    def getNumberOfCylinders(self):
        return self.__numberOfCylinders
    
    #function to update number of cylinders
    def setNumberOfCylinders(self, cylinders):
        self.__numberOfCylinders = cylinders
        
    #function to emission
    def getEmission(self):
        return self.__emission
    
    #function to update emission
    def setEmission(self, emission):
        self.__emission = emission
      
    #print all values as a string   
    def __repr__(self):
        #return all values which need to be sdisplayed
        return '\nRegistration No: ' + self.getReg() + ' ' +'\n\
Make: ' + self.getMake() + ' ' +'\n\
Colour: ' + self.getColour() + ' ' +'\n\
Mileage: ' + self.getMileage() + ' ' +'\n\
Horse Power: ' + self.getHorsePower() + ' ' +'\n\
Cylinders: ' + self.getNumberOfCylinders() + ' ' +'\n\
Emission: ' + self.getEmission() + '\n'
        
#set diesel car class, insert class car as parameter
#diesel car class should have unique private parameters
class DieselCar(Car):
    
    def __init__(self, reg = '', make = '', colour = '', mileage = 0, horsePower = 0,  emisson = 0, turbo = ''):
        #call car class, car class should have all required parameters for each car
        Car.__init__(self, make, colour, mileage, horsePower, reg)
        self.__emission = emisson
        self.__turbo = turbo
        
    #function to emission
    def getEmission(self):
        return self.__emission
    
    #function to update emission
    def setEmission(self, emission):
        self.__emission = emission

    #check if vehicle is trubo
    def getTurbo(self):
        return self.__turbo
    
    #function to update emission
    def setTurbo(self, turbo):
        self.__turbo = turbo
        
    #print all values as a string   
    def __repr__(self):
        #return all values which need to be sdisplayed
        return '\nRegistration No: ' + self.getReg() + ' ' +'\n\
Make: ' + self.getMake() + ' ' +'\n\
Colour: ' + self.getColour() + ' ' +'\n\
Mileage: ' + self.getMileage() + ' ' +'\n\
Horse Power: ' + self.getHorsePower() + ' ' +'\n\
Emission: ' + self.getEmission() + ' ' +'\n\
Turbo or not turbo (T/NT): ' + self.getTurbo() + '\n'



#set hybrid car class, insert class car as parameter
#hybrid car class should have unique private parameters
class HybridCar(Car):
    
    def __init__(self, reg = '', make = '', colour = '', mileage = 0, horsePower = 0, drivingHours = 0, batteries = 1, emisson = 0,):
        #call car class, car class should have all required parameters for each car
        Car.__init__(self, make, colour, mileage, horsePower, reg)
        self.__emission = emisson
        #set how long electric car can drive while fully charged
        self.__drivingHours = drivingHours
        #set how many baterries vehicle has
        self.__amountOfChargebablebatteries = batteries
        
    #get hours how long car can drive while fully charged 
    def getDrivingHours(self):
        return self.__drivingHours
    
    #set how long car can drive while fully charged
    def setDrivingHours (self, hours):
        self.__drivingHours = hours
        
    #get amount of baterries in vehicile 
    def getAmountOfChargebablebatteries(self):
        return self.__amountOfChargebablebatteries
    
    #set amount of baterries in vehicile
    def setAmountOfChargebablebatteries (self, batteries):
        self.__amountOfChargebablebatteries = batteries 


    #function to emission
    def getEmission(self):
        return self.__emission
    
    #function to update emission
    def setEmission(self, emission):
        self.__emission = emission
        
    #print all values as a string   
    def __repr__(self):
        #return all values which need to be sdisplayed
        return '\nRegistration No: ' + self.getReg() + ' ' +'\n\
Make: ' + self.getMake() + ' ' +'\n\
Colour: ' + self.getColour() + ' ' +'\n\
Mileage: ' + self.getMileage() + ' ' +'\n\
Horse Power: ' + self.getHorsePower() + ' ' +'\n\
Drving houts then battery charged: ' + self.getDrivingHours() + ' ' +'\n\
Amount of chargable batteries: ' + self.getAmountOfChargebablebatteries() +  ' ' +'\n\
Emission: ' + self.getEmission() + '\n'


#if run from the command line print code which is below
#test code must be write below, and it won't be shown in the interactive part of the code
if __name__ == '__main__':
    unittest.main()