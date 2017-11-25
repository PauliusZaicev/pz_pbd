from calculator import Calculator

import os
os.chdir('D://DBS//5.Programming_for_big_data//github//pz_pbd//CA5')
# testing method by which individual units of source code


#print out msgs
input1 = '        Please enter numbers for a 1st list'
input2 = '        Please enter numbers for a 2nd list'
input_one_list = '        Please enter numbers to the list'


#exit program once done typed
def done (val):
    return val != ('done').lower()
            
            
#create function which would return a one list 
#creating this funstion separetely,to emplement behavior for each list
#and going to use for separate imputs
def add_to_list():
    input_one_list = ''
    list3 = []
    while done(input_one_list):
        input_one_list = ' Please enter numbers for a list\n\
 Each number must be separated by comma: '
        input_one_list = raw_input(input_one_list)
        #strip and split inserted values
        input_one_list = input_one_list.strip().split(',')
        try:        
            for value in input_one_list:
                value = float(value)
                list3.append(value)
            #print '\nAdded list displayed below:'
            return list3
        except:
            print '\n Please enter numeric values and separate each value by using comma! \n\
 \n NOTE: Previuosly added numeric values are appended into the list'

#print add_to_list()
            
            
#create function which would return a one list 
#creating this funstion separetely,to emplement behavior for each list
#and going to use for separate imputs
def add_to_1stlist():
    input1 = ''
    list1 = []
    while done(input1):
        input1 = ' Please enter numbers for a 1st list\n\
 Each number must be separated by comma: '
        input1 = raw_input(input1)
        #strip and split inserted values
        input1 = input1.strip().split(',')
        try:        
            for value in input1:
                value = float(value)
                list1.append(value)
            #print '\nFirst list displayed below:'
            return list1
        except:
            print ' \n Please enter numeric values and separate each value by using comma! \n\
 \n NOTE: Previuosly added numeric values are appended into the list'
            
#print add_to_1stlist()


#create function which would return a one list 
#creating this funstion separetely,to emplement behavior for each list
#and going to use for separate imputs
def add_to_2ndlist():
    input2 = ''
    list2 = []
    while done(input):
        input2 = ' Please enter numbers for a 2nd list\n\
 Each number must be separated by comma: '
        input2 = raw_input(input2)
        #strip and split inserted values
        input2 = input2.strip().split(',')
        try:        
            for value in input2:
                value = float(value)
                list2.append(value)
            #print '\nFirst list displayed below:'
            return list2
        except:
            print ' \n Please enter numeric values and separate each value by using comma! \n\
 \n NOTE: Previuosly added numeric values are appended into the list'

#print add_to_2ndlist() <- Test           
     
            
            

#menu option in the calculator
def menu_o():
    menu_option = ''
    #while menu option not done continue
    while done(menu_option):
        #display menu options
        print 'Please select below:\n\
        1 - to add two lists\n\
        2 - to subtract\n\
        3 - to divide\n\
        4 - to multiply\n\
        5 - first value to the power of the second value\n\
        6 - cubic value of the number\n\
        7 - ten to power of inserted number\n\
        8 - square root\n\
        9 - cubic root\n\
        10 - muliply first value by the 10 power to the second value (x * 10**y)\n'
        menu_option = raw_input('Please enter the option: ')
        menu_option = menu_option.lower()
        if done(menu_option):
            try:
                #convert input to int
                menu_option = int(menu_option)
                #if value inseted whinin the range, print below statement
                if menu_option > 0 and menu_option <= 10:
                    print 'Below option selected: '
                    return menu_option
                #else print error
                else:
                    print 'Pelase enter value between 1 and 10 or type DONE to exit\n'
            except:
                print 'Incorect input, please enter value between 1 and 10'

#create function to check input and bring relevant function from the calculator class
def use_calculator(menu_option):
    msg = ''
    number1 = ''
    number2 = ''
    #while one of the values are not equal to done, continue
    while done (menu_option) and done(msg) and done(number1) and done(number2):
        #import calculator
        from calculator import Calculator
        calculator = Calculator()
        #according to the optuion bring relevant equation and relevant queations to finish equation
        #addition
        if menu_option == 1:
            #assign function for a first list
            l1 = add_to_1stlist()
            #assign function for a first list
            l2 = add_to_2ndlist()
            try:
                #check if both lists are thre same lenght then return the answer
                if len(l1) == len (l2):
                    return ' \n Additon: ' + str(calculator.add(l1, l2))
                #else print error
                else:
                    print ' Please enter two lists with a same length'
            except:
                print ' Please enter two lists with a same length'
        #SUBTARCTION
        elif menu_option == 2:
            #assign function for a first list
            l1 = add_to_1stlist()
            #assign function for a first list
            l2 = add_to_2ndlist()
            try:
                #check if both lists are thre same lenght then return the answer
                if len(l1) == len (l2):
                    return ' \n Subtraction: ' + str(calculator.subtract(l1, l2))
                #else print error
                else:
                    print ' Please enter two lists with a same length'
            except:
                print ' Please enter two lists with a same length'   
        #dividion
        elif menu_option == 3:
            #assign function for a first list
            l1 = add_to_1stlist()
            #assign function for a first list
            l2 = add_to_2ndlist()
            try:
                #check if both lists are thre same lenght then return the answer
                if len(l1) == len (l2):
                    return ' \n Dividion: ' + str(calculator.divide(l1, l2))
                #else print error
                else:
                    print ' Please enter two lists with a same length'
            except:
                print ' Please enter two lists with a same length'
        #multiplication
        elif menu_option == 4:
            #assign function for a first list
            l1 = add_to_1stlist()
            #assign function for a first list
            l2 = add_to_2ndlist()
            try:
                #check if both lists are thre same lenght then return the answer
                if len(l1) == len (l2):
                    return ' \n Multiplication: ' + str(calculator.multiply(l1, l2))
                #else print error
                else:
                    print ' Please enter two lists with a same length'
            except:
                print ' Please enter two lists with a same length'
        #exponential
        elif menu_option == 5:
            #assign function for a first list
            l1 = add_to_1stlist()
            #assign function for a first list
            l2 = add_to_2ndlist()
            try:
                #check if both lists are thre same lenght then return the answer
                if len(l1) == len (l2):
                    return ' \n Exponential: ' + str(calculator.exponantial(l1, l2))
                #else print error
                else:
                    print ' Please enter two lists with a same length'
            except:
                print ' Please enter two lists with a same length'
        #cubic
        elif menu_option == 6:
            #assign function for a first list
            l1 = add_to_list()
            #return result
            return ' \n Cubic value: ' + str(calculator.cube(l1))
        #ten to power to inserted value
        elif menu_option == 7:
            #assign function for a first list
            l1 = add_to_list()
            #return result
            return ' \n Ten to power of inserted value: ' + str(calculator.ten_to_power(l1))
        #square root
        elif menu_option == 8:
            #assign function for a first list
            l1 = add_to_list()
            #return result
            return ' \n Square root: ' + str(calculator.sqr(l1))
        #cuboc root of the value
        elif menu_option == 9:
            #assign function for a first list
            l1 = add_to_list()
            #return result
            return ' \n Cubic root: ' + str(calculator.cubicr(l1))
        #Muliply first value by the 10 power to the second value
        elif menu_option == 10:
            #assign function for a first list
            l1 = add_to_1stlist()
            #assign function for a first list
            l2 = add_to_2ndlist()
            try:
                #check if both lists are thre same lenght then return the answer
                if len(l1) == len (l2):
                    return ' \n Muliply first value by the 10 power to the second value: '\
                + str(calculator.value_multiply_to_ten_power(l1, l2))
                #else print error
                else:
                    print ' Please enter two lists with a same length'
            except:
                print ' Please enter two lists with a same length'

        
#cal calcualtor and continue
def calculator():  
    msg = ''    
    while done(msg):
        #assigne menu function to variable
        menu = menu_o()
        #print menu
        print menu
        #insert menu option into use_calculator function
        use_calculator_variable = use_calculator(menu)
        print use_calculator_variable
        #input 1 to continue and 0 to exit
        msg = raw_input('Pelase press:\n 0 to Exit\n 1 to continue\n Pelase enter your option:')
        try:
            #check if input is 0 or 1
            msg = int(msg)
            #if 0 exit calculator
            if msg == 0:
                return 'Thank you very much for using my calculator!'
            #if 1 continue
            elif msg == 1:
                print menu
                print use_calculator_variable
            else:
                #else print msg variable
                print msg
        #else print except msg
        except:
            print msg
                
#call calculator function
print calculator()


       
#create function which would return a one list with insertet option
'''  def add_to_list(entry):
    original_entry = entry
    list1 = []
    while done(original_entry):
        original_entry =  str(entry) + '\n\
        Each number must be separated by comma: '
        entry = raw_input(original_entry)
        #strip and split inserted values
        split_values = entry.strip().split(',')
        try:        
            for value in split_values:
                value = float(value)
                list1.append(value)
            print '\nList displayed below:'
            return list1
        except:
            print 'Please enter numeric values and separate each value by using comma'

print add_to_list(input_one_list)            
print add_to_list(input1)  
print add_to_list(input2) '''