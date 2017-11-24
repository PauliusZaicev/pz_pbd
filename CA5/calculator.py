'''C5 b)'''

import os
os.chdir('D://DBS//5.Programming_for_big_data//github//pz_pbd//CA5')

class Calculator(object):
    
    #addition function
    def add (self, first, second):
        return map(lambda x,y:x+y, first,second)
    
    #subtract function
    def subtract(self, first, second):
        return map(lambda x,y: x-y, first, second)
    
      
    #multiply fuction
    def multiply (self, first, second):
        return map(lambda x,y: x*y, first, second)

    #divide function   
    def divide (self, first, second):
        return map(lambda x,y: 'nan' if y == 0 else x/float(y), first, second)
    
    #ten to power
    def ten_to_power(self, first):
        return map(lambda x: 10**x, first)
    
    
    #squere root function
    def sqr(self,first):
        import math
        return map(lambda x: 'nan' if x < 0 else math.sqrt(x), first)
    
    #cubic root function      
    def cubicr(self,first):
        return map(lambda x: x**(1./3.) if 0<=x else -(-x)**(1./3.), first)
    
    
    #cube function
    def cube(self, first):
        return map(lambda x: x**3, first)
    
    
    #x to power of y        
    def exponantial(self, first, second):
        return map(lambda x, y: x**y, first, second)
    
    #get value for x * (10**y)
    def value_multiply_to_ten_power (self, first, second):
        return map(lambda x,y: x * (10**y), first, second)



