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
 
        #test divide functions from calculator class
    def test_calculator_divide(self):
        result = Calculator().divide([2,4,5,6],[2,4,5,6])
        self.assertEqual([1.0,1.0,1.0,1.0],result)
        result = Calculator().divide([5,9,5,8],[2,3,5,2])
        self.assertEqual([2.5,3.0,1.0,4.0],result)
        result = Calculator().divide([5,-9,5,-8],[0.2,3,-1,-2])
        self.assertEqual([25.0,-3.0,-5.0,4.0], result)  
        result = Calculator().divide([0,2,3,4], [1,2,0,4])
        self.assertEqual([0.0, 1.0, 'nan', 1.0], result)
  
    
    #test ten to power of the list number
    def test_calculator_ten_to_power(self):
        result = Calculator().ten_to_power([0,4,-4,4.5])
        self.assertEqual([1, 10000, 0.0001, 31622.776601683792],result)

    #cubic root test
    def test_calculator_cubicr(self):
        result = Calculator().cubicr([8, 15.625, 0, -8])
        self.assertEqual([2.0, 2.5, 0.0, -2.0],result)


    #test cube of the inserted numebr
    def test_calculator_cube(self):
        result = Calculator().cube([8, -8, 0, -1, 1, 2.5])
        self.assertEqual([512, -512, 0, -1, 1, 15.625],result)
        
    #test exponential
    def test_calculator_exponantial(self):
        result = Calculator().exponantial([-2,-4,6,7, 4, 0, 2.5],[2,-4,6,7, 0, 4, 2.5])
        self.assertEqual([4, 0.00390625, 46656, 823543, 1, 0, 9.882117688026185],result)
        
    #formula - x * 10**y
    def test_calculator_value_multiply_to_ten_power(self):
        result = Calculator().value_multiply_to_ten_power([5,-5,0,1,-6,6], [5,-1,1,0,2,-2])
        self.assertEqual([500000, -0.5, 0, 1, -600, 0.06],result)
    
'''

        
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

