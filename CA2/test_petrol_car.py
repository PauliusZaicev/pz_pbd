import os
os.chdir('D://DBS//5.Programming_for_big_data//Car//CA')


#import unittest to test Electric car class
import unittest

#import from car , car class
from car import Car
#import from car, petrol class
from car import PetrolCar


# test the car functionality
class TestCar(unittest.TestCase):
    #special function, setUp function runs first before any test
    def setUp(self):
        #need to check for each class sepetrately
        #set car to electric car class
        self.car = PetrolCar()
    
    #test mileage
    def test_car_mileage(self):
        #start mileage equal to 0
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
    
       
    #test number of cylinders
    def test_number_of_cylinders(self):
        #number of cells equal to 1
        self.assertEqual(1, self.car.getNumberOfCylinders())
        #update numebr of cylinders to 2
        self.car.setNumberOfCylinders(2)
        #number of cells changed from 1 to 15
        self.assertEqual(2, self.car.getNumberOfCylinders())
        
    #test emission
    def test_emission(self):
        #emission equal to 0
        self.assertEqual(0, self.car.getEmission())
        #update emission to 160
        self.car.setEmission(160)
        #emission changed from 1 tto 160
        self.assertEqual(160, self.car.getEmission())
    

if __name__ == '__main__':
    unittest.main()