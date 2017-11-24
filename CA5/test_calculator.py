#from the calculator import calculator class, files should be in the same directory
from calculator import Calculator

import os
os.chdir('D://DBS//5.Programming_for_big_data//github//pz_pbd//CA5')
# testing method by which individual units of source code
import unittest


class Testcalculator(unittest.TestCase):
    #rules, function should have test at the begining
    
        #test addition
    def test_calculator_add(self):
        result = Calculator().add([1,2,3,4], [1, 2, 3, 4])
        #assert gives possible answers
        self.assertEqual([2,4,6,8],result)
        result = Calculator().add([-1,2,-3,4, 0], [1, 2, 4, 3, -2])
        #assert gives possible answers
        self.assertEqual([0,4,1,7,-2],result)
        #if string in the list test should fail
        try:
            result = Calculator().add(['a',2,3,4],['a',2,3,4])
        except ValueError:
            #if fales lets pass as it is correct
            pass
        
        #test supraction
    def test_calculator_subtract(self):
        result = Calculator().subtract([2,8,6,9], [4,6,9,5])
        self.assertEqual([-2,2,-3,4],result)
        result = Calculator().subtract([0,0,0,0],[-9,-8,4,5])
        self.assertEqual([9,8,-4,-5],result)

        #test multiplication
    def test_calculator_multiply(self):
        result = Calculator().multiply([2,4,5,6],[2,4,5,6])
        self.assertEqual([4,16,25,36],result)
        result = Calculator().multiply([-2,-4,-5,-6],[2,4,5,6])
        self.assertEqual([-4,-16,-25,-36],result)
        result = Calculator().multiply([-2,-4,-5,-6],[-2,-4,-5,-6])
        self.assertEqual([4,16,25,36],result)
        result = Calculator().multiply([2.0,4.0,5.0,6.0],[2,4,5,6])
        self.assertEqual([4.0,16.0,25.0,36.0],result)
 
        
        

    '''
    #test divide funcrtion from calculator class
    def test_calculator_divide(self):
        #assigne clas and state a function u want to test, after insert required amount of parameters
        result = Calculator().divide(5,5)
        #then function runs in self.asserEqual you need insert right answer in the first parameter (ex 5/5 = 1)
        #in the second parameter you need to insert variable result in which equation was assigned
        self.assertEqual(1,result)
        result = Calculator().divide(5,1)
        self.assertEqual(5,result)
        result = Calculator().divide(5,0.2)
        self.assertEqual(25,result)   
        result = Calculator().divide(5,4)
        self.assertEqual(1.25,result)
        result = Calculator().divide(5,0)
        #devide by 0 is not piossible, for this reason program should return nan as per main calculator class
        self.assertEqual('nan',result)
    
     
     

        

        
    #test exponential
    def test_calculator_exponantial(self):
        result = Calculator().exponantial(5,5)
        self.assertEqual(3125,result)
        result = Calculator().exponantial(5,0)
        self.assertEqual(1,result)
        result = Calculator().exponantial(4,-2)
        self.assertEqual(0.0625,result)
        result = Calculator().exponantial(-2,5)
        self.assertEqual(-32,result)
        result = Calculator().exponantial(5,2)
        self.assertEqual(25,result)
        #if string inserted shoudl fail
        try:
            result = Calculator().add('2','5')
            #if shows print it is bad because it can't add strings
            self.fail('Should have thrown error')
        except ValueError:
            pass
        
    #test squere root    
    def test_calculator_sqr(self):
        result = Calculator().sqr(25)
        self.assertEqual(5,result)
        #squere root of negative value not possible, so class return nan
        result = Calculator().sqr(-9)
        self.assertEqual('nan',result)
        result = Calculator().sqr(9)
        self.assertEqual(3,result)
        try:
            result = Calculator().sqr('2')
            #if shows print it is bad because it can't add strings
            self.fail('Should have thrown error')
        except ValueError:
            pass
        
    #test cube of the inserted numebr
    def test_calculator_cube(self):
        result = Calculator().cube(3)
        self.assertEqual(27,result)
        result = Calculator().cube(-9)
        self.assertEqual(-729,result)
        result = Calculator().cube(0)
        self.assertEqual(0,result)
        try:
            result = Calculator().cube('2')
            #if shows print it is bad because it can't add strings
            self.fail('Should have thrown error')
        except ValueError:
            pass
        
    #set ten to power of insertet numeber
    def test_calculator_ten_to_power(self):
        result = Calculator().ten_to_power(3)
        self.assertEqual(1000,result)
        result = Calculator().ten_to_power(-1)
        self.assertEqual(0.1,result)
        result = Calculator().ten_to_power(0)
        self.assertEqual(1,result)
        result = Calculator().ten_to_power(1)
        self.assertEqual(10,result)
        try:
            result = Calculator().ten_to_power('2')
            #if shows print it is bad because it can't add strings
            self.fail('Should have thrown error')
        except ValueError:
            pass
        
    #formula - x * 10**y
    def test_calculator_value_multiply_to_ten_power(self):
        result = Calculator().value_multiply_to_ten_power(5,5)
        self.assertEqual(500000,result)
        result = Calculator().value_multiply_to_ten_power(-5,-1)
        self.assertEqual(-0.5,result)
        result = Calculator().value_multiply_to_ten_power(0, 1)
        self.assertEqual(0,result)
        result = Calculator().value_multiply_to_ten_power(1,0)
        self.assertEqual(1,result)
        result = Calculator().value_multiply_to_ten_power(-6,2)
        self.assertEqual(-600,result)
        result = Calculator().value_multiply_to_ten_power(6,-2)
        self.assertEqual(0.06,result)
        try:
            result = Calculator().value_multiply_to_ten_power('2', '5')
            #if shows print it is bad because it can't add strings
            self.fail('Should have thrown error')
        except ValueError:
            pass
    
    #cubic root
    def test_calculator_cubicr(self):
        result = Calculator().cubicr(8)
        self.assertEqual(2,result)
        result = Calculator().cubicr(15.625)
        self.assertEqual(2.5,result)
        result = Calculator().cubicr(0)
        self.assertEqual(0,result)
        result = Calculator().cubicr(-8)
        self.assertEqual(-2,result)
        try:
            result = Calculator().cubicr('2')
            #if shows print it is bad because it can't add strings
            self.fail('Should have thrown error')
        #pass if prins error
        except ValueError:
            pass
        
        
'''
'''
5

Internally, unittest.main() is using a few tricks to figure out the name of the
module (source file) that contains the call to main().
It then imports this modules, examines it, gets a list of 
all classes and functions which could be tests (according the configuration) 
and then creates a test case for each of them.

When the list is ready, it executes each test in turn.'''
if __name__ == '__main__':
    unittest.main()

