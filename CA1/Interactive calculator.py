#print out msgs
input1 = 'Please enter 1st number: '
input2 = 'Please enter 2nd number: '
input_one_numb = 'Please enter number: '


#exit program once done typed
def done (val):
    return val != ('done').lower()

#menu option in the calculator
def menu_o():
    menu_option = ''
    #while menu option not done continue
    while done(menu_option):
        #display menu options
        print 'Please select below:\n\
        1 - to add two numbers\n\
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
            number1 = raw_input(input1)
            number2 = raw_input(input2)        
            try:
                #only add if both are numbers
                number1 = float(number1) or int(number1) or long(number1) or complex(number1)
                number2 = float(number2) or int(number2) or long(number2) or complex(number2)
                #retiurn answer
                return 'Additon: ' + str(calculator.add(number1, number2))
            except:
                #if not number print below messege
                print 'Please enter integer'
        #SUBTARCTION
        elif menu_option == 2:
            number1 = raw_input(input1)
            number2 = raw_input(input2)
            try:
                #only add if both are numbers
                number1 = float(number1) or int(number1) or long(number1) or complex(number1)
                number2 = float(number2) or int(number2) or long(number2) or complex(number2)
                #Rreturn subtraction
                return 'Subtraction: ' + str(calculator.subtract(number1, number2))
            except:
                #if not number print below messege
                print 'Please enter integer'
        #dividion
        elif menu_option == 3:
            number1 = raw_input(input1)
            number2 = raw_input(input2)
            try:
                #only add if both are numbers
                number1 = float(number1) or int(number1) or long(number1) or complex(number1)
                number2 = float(number2) or int(number2) or long(number2) or complex(number2)
                #return dividion
                return 'Dividion:' + str(calculator.divide(number1, number2))
            except:
                #if not number print below messege
                print 'Please enter integer'
        #multiplication
        elif menu_option == 4:
            number1 = raw_input(input1)
            number2 = raw_input(input2)
            #only add if both are numbers
            try:
                #only add if both are numbers
                number1 = float(number1) or int(number1) or long(number1) or complex(number1)
                number2 = float(number2) or int(number2) or long(number2) or complex(number2)
                return 'Multiplication:' + str(calculator.multiply(number1, number2))
            except:
                #if not number print below messege
                print 'Please enter integer'
        #exponential
        elif menu_option == 5:
            number1 = raw_input(input1)
            number2 = raw_input(input2)
            try:
                #only add if both are numbers
                number1 = float(number1) or int(number1) or long(number1) or complex(number1)
                number2 = float(number2) or int(number2) or long(number2) or complex(number2)
                #return exponential
                return 'Exponential: ' + str(calculator.exponantial(number1, number2))
            except:
                #if not number print below messege
                print 'Please enter integer'
        #cubic
        elif menu_option == 6:
            number1 = raw_input(input_one_numb)
            try:
                #only add if both are numbers
                number1 = float(number1) or int(number1) or long(number1) or complex(number1)
                #return cubic value
                return 'Cubic value: ' + str(calculator.cube(number1))
            except:
                #if not number print below messege
                print 'Please enter integer'
        #ten to power to inserted value
        elif menu_option == 7:
            number1 = raw_input(input_one_numb)
            try:
                #only add if both are numbers
                number1 = float(number1) or int(number1) or long(number1) or complex(number1) 
                #return ten to power of inserted value
                return 'Ten to power of inserted value: ' +str(calculator.ten_to_power(number1))
            except:
                #if not number print below messege
                print 'Please enter integer'
        #square root
        elif menu_option == 8:
            number1 = raw_input(input_one_numb)
            try:
                #only add if both are numbers
                number1 = float(number1) or int(number1) or long(number1) or complex(number1)
                #square root
                return 'Square root: ' + str(calculator.sqr(number1))
            except:
                #if not number print below messege
                print 'Please enter integer'
        #cuboc root of the value
        elif menu_option == 9:
            number1 = raw_input(input_one_numb)
            try:
                #only add if both are numbers
                number1 = float(number1) or int(number1) or long(number1) or complex(number1)  
                #return cubic root
                return 'Cubic root: ' + str(calculator.cubicr(number1))
            except:
                #if not number print below messege
                print 'Please enter integer'
        #Muliply first value by the 10 power to the second value
        elif menu_option == 10:
            number1 = raw_input(input1)
            number2 = raw_input(input2)
            try:
                #only add if both are numbers
                number1 = float(number1) or int(number1) or long(number1) or complex(number1)
                number2 = float(number2) or int(number2) or long(number2) or complex(number2)
                #return value
                return 'Muliply first value by the 10 power to the second value:' + str(calculator.value_multiply_to_ten_power(number1, number2))
            except:
                #if not number print below messege
                print 'Please enter integer'
        
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