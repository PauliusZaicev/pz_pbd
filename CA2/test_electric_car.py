import os
os.chdir('D://DBS//5.Programming_for_big_data//Car//CA')

#import unittest to test Electric car class
import unittest

#import from car , car class
from car import Car
#import from car, elcticcar class
from car import ElectricCar


# test the car functionality
class TestCar(unittest.TestCase):
    #special function, setUp function runs first before any test
    def setUp(self):
        #need to check for each class sepetrately
        #set car to electric car class
        self.car = ElectricCar()
    
    #test mileage
    def test_car_mileage(self):
        #stat mileage equal to 0
        self.assertEqual(0, self.car.getMileage())
        #move car 15 miles
        self.car.move(15)
        #mileage should increace
        self.assertEqual(15, self.car.getMileage())
        
    #test make
    def test_car_make(self):
        #make is empty
        self.assertEqual('', self.car.getMake())
        #set make tp ferrari
        self.car.setMake('Ferrari')
        #make should return updated value Ferrari
        self.assertEqual('Ferrari', self.car.getMake())
        
    #test colour
    def test_car_colour(self):
        #colour is blank
        self.assertEqual('', self.car.getColour())
        #paint car to red
        self.car.paint('red')
        #must return red colour
        self.assertEqual('red', self.car.getColour())
        
    #test horse power
    def test_horse_power(self):
        #horse power is 0
        self.assertEqual(0, self.car.getHorsePower())
        #change horse power
        self.car.changeHorsePower(110)
        self.assertEqual(110, self.car.getHorsePower())
        
    #test reg function
    def test_reg(self):
        #reg is 0
        self.assertEqual('', self.car.getReg())
        #change a reg
        self.car.changeReg('151D52')
        #get updated reg
        self.assertEqual('151D52', self.car.getReg())
    
       
    #test number of cells
    def test_car_number_of_fuel_cells(self):
        #number of cells equal to 1
        self.assertEqual(1, self.car.getNumberOfFuelCells())
        #update numebr of cells to 15
        self.car.setNumberOfFuelCells(15)
        #number of cells changed from 1 to 15
        self.assertEqual(15, self.car.getNumberOfFuelCells())
        
     #test driving hours the battery charged   
    def test_driving_hours(self):
        #number of driving hours equal to 0
        self.assertEqual(0, self.car.getDrivingHours())
        #update numebr of driving hours to 20
        self.car.setDrivingHours(20)
        #hours should change to 20
        self.assertEqual(20, self.car.getDrivingHours())
        
        
    #amount of chargebale battries    
    def test_amount_of_chargebable_batteries(self):
        #number of batteries 1
        self.assertEqual(1, self.car.getAmountOfChargebablebatteries())
        #update numeber of batteries
        self.car.setAmountOfChargebablebatteries(3)
        #show updated amount of batteries
        self.assertEqual(3, self.car.getAmountOfChargebablebatteries())

if __name__ == '__main__':
    unittest.main()
