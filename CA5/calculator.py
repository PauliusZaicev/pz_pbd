'''C1'''

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


'''    
    #x to power of y        
    def exponantial(self, x, y):
        #define number types
        number_types = (int, long, float, complex)
        #only proceed if value type can be set as per number_types variable
        if isinstance(x, number_types) and isinstance(y, number_types):
            #retuern x to power of y
            return x**y
        #if type of value incorect return error
        else:
            raise ValueError        
    
    
    def divide (self, x, y):
        #define number types
        number_types = (int, long, float, complex)
        #only proceed if value type can be set as per number_types variable
        if isinstance(x, number_types) and isinstance(y, number_types):
            #if y equal to 0 return nan
            if y == 0:
                return 'nan'
            else:
                #else return dividion
                return x / float(y)
        #if type of value incorect return error
        else:
            raise ValueError
    

    


    #squere root
    def sqr(self,x):
        #import math to get square 
        import math
        #define number types
        number_types = (int, long, float, complex)
        
        #if value less than 0 return nan
        if isinstance(x, number_types) :
            if x < 0:
                #if x less than 0 return nan
                return 'nan'
            #if value more than 0 return sqrt
            else:
                return math.sqrt(x)
        #if type of value incorectr return error
        else:
            raise ValueError
    
    #cube of the inserted number
    def cube(self, x):
        #define number types
        number_types = (int, long, float, complex)
        
        #return inserted value to the power of three
        if isinstance(x, number_types):
            #is x type in number types return cube
            return x**3
        #if type of value incorectr return error
        else:
            raise ValueError
    
    #ten to power of inserten numeber
    def ten_to_power(self, x):
        #define number types
        number_types = (int, long, float, complex)
        #only proceed if value type can be set as per number_types variable
        if isinstance(x, number_types):
            #if x instance in numebr types return 10 to power of x
            return 10**x
        #if type of value incorectr return error
        else:
            raise ValueError
    
    #get value for x * (10**y)
    def value_multiply_to_ten_power (self, x, y):
        #define number types
        number_types = (int, long, float, complex)
        #only proceed if value type can be set as per number_types variable
        if isinstance(x, number_types) and isinstance(y, number_types):
            #if both numebers in instance return answer
            return x * (10**y)
        #if type of value incorectr return error
        else:
            raise ValueError
            
    #cubic root       
    def cubicr(self,x):
        #define number types
        number_types = (int, long, float, complex)
        #only proceed if value type can be set as per number_types variable
        if isinstance(x, number_types) :
            if 0 <= x:
                #for positive x value return value then x positive
                return x**(1./ 3.)
            #for negative value insert x as negative value
            return -(-x)**(1./ 3.)
        #if type of value incorectr return error
        else:
            raise ValueError
            
'''
#assigne class to the variable    
#calculator = Calculator()
#test calculator
#print calculator.cubicr(-64)
#print calculator.add(5,5)
#print calculator.subtract(5,5)

cal = Calculator()
cal.add([1,2,3,4], [1,2,3,4])
cal.add(['a',2,3,4], ['a',2,3,4])