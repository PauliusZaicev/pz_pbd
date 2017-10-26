#import directory    
import os
os.chdir('D://DBS//5.Programming_for_big_data//Car//CA')


    
#exit program once done typed
def done (val):
    return val != ('done').lower()



#import electric, hybrid, petrol and diesel classes from car file
from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar



#create car dealership class
class Dealership(object):

    #set attributes petrol_cars, electric_cars, diesel_cars and Hybrid_cars to empty lists
    def __init__(self, petrol_cars = [], electric_cars = [], diesel_cars = [], hybrid_cars = []):
        self.petrol_cars = petrol_cars
        self.electric_cars = electric_cars
        self.diesel_cars = diesel_cars
        self.hybrid_cars = hybrid_cars
        self.rentet_petrol_cars = []
        self.rentet_electric_cars = []
        self.rentet_diesel_cars = []
        self.rentet_hybrid_cars = []
        self.petrol_customers = []
        self.electric_customers = []
        self.diesel_customers = []
        self.hybrid_customers = []
        self.customers = []

    #exit, once done typed
    def done (self, val):
        return val != ('done').lower()
    
    #return each value from the car list not as a list, but as a value
    def nice_display (self, cars_list, cust=None):
        #if no customer parameter empty
        if cust is None:
            #for value in the car list print car
            for value in cars_list:
                print value
        #if customer is known        
        else:
            #for value in car list
            for value in cars_list:
                #check a car renter rented
                if value['renter'] == cust:
                    #and return this car
                    print value['car']
    
    #function reads file and updates relevant lists
    def create_stock(self, cars_list):
        #for each line in car list
        for line in cars_list:
            #strip, remove all empty lines and characters ssuch as \n and remove all commas
            values = line.strip().split(',')
            #if first index in the list equal to petrol
            if values [0] == 'Petrol':
                #append petrol car list
                self.petrol_cars.append(PetrolCar(values[1],values[2], values[3], values[4], values[5], values[9],  values[10]))
            #if first index equal to eletric , append electric car list
            elif values[0] == 'Electric':
                #append electric car list with information about electric car
                self.electric_cars.append(ElectricCar(values[1],values[2], values[3], values[4] , values[5] , values[6], values[7], values[8]))
            #if first index equal to diesel , append diesel car list
            elif values[0] == 'Diesel':
                #append diesel car list with information about diesel car
                self.diesel_cars.append(DieselCar(values[1],values[2], values[3], values[4], values[5], values[10], values[11]))
            #if first index equal to hybrid , append hybrid car list
            elif values[0] == 'Hybrid':
                #append hybrid car list with information about hybrid car
                self.hybrid_cars.append(HybridCar(values[1],values[2], values[3], values[4], values[5], values[7], values[8], values[10]))

    #check how many cars we have in stock
    #set a lenght for each type of cars
    def stock_count(self):
        print '\nPetrol cars in stock: ' + str(len(self.petrol_cars))
        print 'Electric cars in stock: ' + str(len(self.electric_cars))
        print 'Diesel cars in stock: ' + str(len(self.diesel_cars))
        print 'Hybrid cars in stock: ' + str(len(self.hybrid_cars))
        
    '''
    Test if stock count displayes allcars
    dealership = Dealership()
    dealership.stock_count(petrol_cars , electric_cars, diesel_cars, hybrid_cars)'''


    #menu option in the app to rent a car, return a car or exit an app
    def menu_o(self):
        menu_option = ''
        #while menu option not done continue
        while done(menu_option):
            #display menu options
            print '\nWelcome to the Aungier Car Rental\n\
            \nPlease select from the below options below:\n\
\n1 - Rent a car\n\
2 - Return a car\n\
3 - Output a file\n\
Type done to quit APP'
            menu_option = raw_input('Please enter the option: ')
            menu_option = menu_option.lower()
            if done(menu_option):
                try:
                    #convert input to int
                    menu_option = int(menu_option)
                    #if value inserted whinin the range, print below statement
                    if menu_option >= 1 and menu_option <= 3:
                        #print 'Below option selected: '
                        return menu_option
                    #else print error
                    else:
                        print '\nPelase enter value between 1 and 2 or type DONE to exit\n'
                except:
                    print '\nIncorect input, please enter value between 1 and 2\n'
            else:
                print '\nThank you for using our APP'



    
    #process rental function
    def process_rental(self):
            question = ''
            answer = ''
            amount = ''
            while done(question) and done(answer) and done(amount):
                #ask if user would like to rent a car
                question = raw_input('Would you like to rent a car or return back to MENU? \n\
\nY - Yes\n\
N - No\n\
\nPlease enter your option: ')
                question = question.lower()
                try:
                    #if answer is yes
                    if question == 'y':
                        #ask what type of car he want to rent
                        question = raw_input('What type would you like?\n\
\nP - Petrol\n\
E - Electric\n\
D - Diesel\n\
H - Hybrid\n\
S - Display stock count\n\
B - Back to MENU\n\
Q - To Quit\n\
\nPlease enter your option: ')
                        question = question.lower()
                        try:
                            #is user select p - petrol car
                            if question == 'p':
                                #if petrol car list is empty
                                if len(self.petrol_cars) <= 0:
                                    #print error message
                                    print 'Sorry nothing to rent, please try again'
                                #else
                                else:
                                    #print all petrol car which are available
                                    self.nice_display (self.petrol_cars)
                                    #cutomers cridentials
                                    cust = raw_input('Please enter your email address: ')
                                    #request to enter the reg number
                                    reg = raw_input('Please enter the reg: ')
                                    #for car in petrol cars list
                                    for car in self.petrol_cars:
                                        #debuging if selected car will be removed
                                        #1print 'reg ' + reg + ' car reg ' + car.getReg()
                                        #2print 'equal ' + str(reg == car.getReg())
                                        #if inserted reg equels to one of the cars reg's(call function from the car get reg)
                                        if reg.lower() == car.getReg().lower():
                                            #debugiong and printing removing
                                            #3print 'removing'
                                            #if one of the reges equal to the car which is in petrol)cars list - remove
                                            self.petrol_cars.remove(car)
                                            #append rentet petrol cars dictionary as car inforamtion and cusrtomer cridentials
                                            self.rentet_petrol_cars.append({'car':car,'renter':cust})
                                            #if customer not in our database
                                            if cust not in self.customers:
                                                #append cutomers list with his cridentials
                                                self.customers.append(cust)
                                            #else thank a customer
                                            else:
                                                print '\nYour cridentials already known to our database. Thank you for renting a car with us again!'
                                            #if car in the list, print messge
                                            print '\nCar sucesfully rentet\n'
                                            #return menu option
                                            return self.option(self.menu_o()) 
                                    #while loop will count how many cars checked and then alst car checked if reg not in the 
                                    #list it will print messege that car is not found in the list
                                    total = 0
                                    #whil list lenght is less than total
                                    while total <= len(self.petrol_cars):
                                        #Count total
                                       total += 1
                                       #if total equal to lenght print messege that reg not in the list
                                       if total == len(self.petrol_cars):
                                           print '\nNo car in the list with this registration number please try again'
                                        
                            #if user selvets electric car
                            elif question == 'e':
                                #if lenght of the list less or equal to 0
                                if len(self.electric_cars) <= 0:
                                    #print error message
                                    print 'Sorry nothing to rent, please try again'
                                else:
                                    #print all electric cars which are available
                                    self.nice_display (self.electric_cars)
                                    #cutomers cridentials
                                    cust = raw_input('Please enter your email address: ')
                                    #request to enter the reg number
                                    reg = raw_input('Please enter the reg: ')
                                    #for car in electric cars list
                                    for car in self.electric_cars:
                                        #if inserted reg equels to one of the cars reges(call function from the car get reg)
                                        if reg.lower() == car.getReg().lower():
                                            #if one of the reges equal to the car which is in petrol)cars list - remove
                                            self.electric_cars.remove(car)
                                            #append rentet petrol cars dictionary
                                            self.rentet_electric_cars.append({'car':car,'renter':cust})
                                            #if customer not in our database
                                            if cust not in self.customers:
                                                #append cutomers list with his cridentials
                                                self.customers.append(cust)
                                            #else thank a customer
                                            else:
                                                print '\nYour cridentials already known to our database. Thank you for renting a car with us again!'
                                            #if car in the list, print messge
                                            print '\nCar sucesfully rentet\n'
                                            #return menu option
                                            return self.option(self.menu_o()) 
                                    #while loop will count how many cars checked and then alst car checked if reg not in the 
                                    #list it will print messege that car is not found in the list
                                    total = 0
                                    #whil list lenght is less than total
                                    while total <= len(self.electric_cars):
                                        #Count total
                                       total += 1
                                       #if total equal to lenght print messege that reg not in the list
                                       if total == len(self.electric_cars):
                                           print '\nNo car in the lsit with this registration number, pelase try again'
                                        

                            #if user select diesel car
                            elif question == 'd':
                                #if lenght of the list less or equal to 0
                                if len(self.diesel_cars) <= 0:
                                    #print error message
                                    print 'Sorry nothing to rent, please try again'
                                #else
                                else:
                                    #print all diesel cars which are available
                                    self.nice_display (self.diesel_cars)
                                    #cutomers cridentials
                                    cust = raw_input('Please enter your email address: ')
                                    #request to enter the reg numebr
                                    reg = raw_input('Please enter the reg: ')
                                    #for car in diesel cars list
                                    for car in self.diesel_cars:
                                        #if inserted reg equels to one of the cars reges(call function from the car get reg)
                                        if reg.lower() == car.getReg().lower():
                                            #if one of the reges equal to the car which is in petrol)cars list - remove
                                            self.diesel_cars.remove(car)
                                            #append rentet petrol cars dictionary
                                            self.rentet_diesel_cars.append({'car':car,'renter':cust})
                                            #if customer not in our database
                                            if cust not in self.customers:
                                                #append cutomers list with his cridentials
                                                self.customers.append(cust)
                                            #else thank a customer
                                            else:
                                                print '\nYour cridentials already known to our database. Thank you for renting a car with us again!'
                                            #if car in the list, print messge
                                            print '\nCar sucesfully rentet\n'
                                            #return menu option
                                            return self.option(self.menu_o()) 
                                    #while loop will count how many cars checked and then alst car checked if reg not in the 
                                    #list it will print messege that car is not found in the list
                                    total = 0
                                    #whil list lenght is less than total
                                    while total <= len(self.diesel_cars):
                                        #Count total
                                       total += 1
                                       #if total equal to lenght print messege that reg not in the list
                                       if total == len(self.diesel_cars):
                                           print '\nNo car in the list with this registration number, pelase try again'
                                        
                            #if user selects hybrid car
                            elif question == 'h':
                                #if lenght 0 or less
                                if len(self.hybrid_cars) <= 0:
                                    #print error message
                                    print 'Sorry nothing to rent, please try again'
                                #else
                                else:
                                    #print all hybrid cars which are available
                                    self.nice_display (self.hybrid_cars)
                                    #cutomers cridentials
                                    cust = raw_input('Please enter your email address: ')
                                    #request to enter the reg numebr
                                    reg = raw_input('Please enter the reg: ')
                                    #for car in hybrid cars list
                                    for car in self.hybrid_cars:
                                        #if inserted reg equels to one of the cars reges(call function from the car get reg)
                                        if reg.lower() == car.getReg().lower():
                                            #if one of the reges equal to the car which is in petrol)cars list - remove
                                            self.hybrid_cars.remove(car)
                                            #append rentet petrol cars dictionary
                                            self.rentet_hybrid_cars.append({'car':car,'renter':cust})
                                            #if customer not in our database
                                            if cust not in self.customers:
                                                #append cutomers list with his cridentials
                                                self.customers.append(cust)
                                            #else thank a customer
                                            else:
                                                print '\nYour cridentials already known to our database. Thank you for renting a car with us again!'
                                            #if car in the list, print messge
                                            print '\nCar sucesfully rentet\n'
                                            #return menu option
                                            return self.option(self.menu_o()) 
                                    #while loop will count how many cars checked and then alst car checked if reg not in the 
                                    #list it will print messege that car is not found in the list
                                    total = 0
                                    #whil list lenght is less than total
                                    while total <= len(self.hybrid_cars):
                                        #Count total
                                       total += 1
                                       #if total equal to lenght print messege that reg not in the list
                                       if total == len(self.hybrid_cars):
                                           print '\nNo car in the list with this registration number, pelase try again'
                            #if user selcts stock count
                            elif question == 's':
                                #print stock count
                                self.stock_count()
                            #if user selects back to menu option
                            elif question == 'b':
                                #return self option function
                                return self.option(self.menu_o())
                            #insert q to quit
                            elif question == 'q':
                                print '\nYou just quit a rental App'
                                return 'done'
                            #else print wrong input
                            else:
                                print '\nWrong input'
                        except:
                            print question
                    elif question == 'n':
                        #if user enter n program exits
                        print '\nThank you for using our rental sevices'
                        return 'done'
                    #asdd option to return back to the menu
                except:
                    print 'Please enter y/n'
                    
    #process ret5urn function
    def process_return(self):
            question = ''
            answer = ''
            amount = ''
            while done(question) and done(answer) and done(amount):
                #ask if user would like to rent a car
                question = raw_input('Would you like to return a car or return back to MENU? \n\
\nY - Yes\n\
N - No\n\
\nPlease enter your option: ')
                question = question.lower()
                try:
                    #if answer is y
                    if question == 'y':
                        #ask what yypo of car he want to rent
                        question = raw_input('What type would you like?\n\
\nP - Petrol\n\
E - Electric\n\
D - Diesel\n\
H - Hybrid\n\
B - Back to MENU\n\
Q - To Quit\n\
\nPlease enter your option:')
                        question = question.lower()
                        try:
                            #if cutomer wants to return petrol car
                            if question == 'p':
                                #if lenght of rentet cars equal or less than 0
                                if len(self.rentet_petrol_cars) <= 0:
                                    #error messege is printed
                                    print 'No Petrol cars are rentet'
                                #else
                                else:
                                    #cutomers cridentials
                                    cust = raw_input('Please enter your email address: ')
                                    if cust in self.customers:
                                        #print all cars which are in rented cars list
                                        self.nice_display (self.rentet_petrol_cars, cust)
                                        #insert registration numebr
                                        reg = raw_input('Please enter the reg: ')
                                        #check each car in rented cars list
                                        for car in self.rentet_petrol_cars:
                                            #if reg in rented cars list
                                            if reg.lower() == car['car'].getReg().lower():
                                                #remove from the rented cars list
                                                self.rentet_petrol_cars.remove(car)
                                                #add back to the cars list
                                                self.petrol_cars.append(car)
                                                #if car in the list, print messge
                                                print '\nCar sucesfully returned\n'
                                                #return menu option
                                                return self.option(self.menu_o()) 
                                        #while loop will count how many cars checked and then alst car checked if reg not in the 
                                        #list it will print messege that car is not found in the list
                                        total = 0
                                        #whil list lenght is less than total
                                        while total <= len(self.rentet_petrol_cars):
                                            #Count total
                                           total += 1
                                           #if total equal to lenght print messege that reg not in the list
                                           if total == len(self.rentet_petrol_cars):
                                               print 'No car in the return list with this registration number, pelase try again'
                                    else:
                                        print '\nThis customer is not found in our database, pelase try again'
                                            
                            #if customer wants to return electric car
                            elif question == 'e':
                                #if lenght of rentet cars equal or less than 0
                                if len(self.rentet_electric_cars) <= 0:
                                    #error messege is printed
                                    print '\nNo electric cars are rentet'
                                else:
                                    #cutomers cridentials
                                    cust = raw_input('Please enter your email address: ')
                                    if cust in self.customers:
                                        #print all cars which are in rented cars list and rented by this cust
                                        self.nice_display (self.rentet_electric_cars, cust)
                                        #insert registration numebr
                                        reg = raw_input('Please enter the reg: ')
                                        #check each car in rented cars list
                                        for car in self.rentet_electric_cars:
                                            #if reg in rented cars list
                                            if reg.lower() == car['car'].getReg().lower():
                                                #remove from the rented cars list
                                                self.rentet_electric_cars.remove(car)
                                                #add back to the cars list
                                                self.electric_cars.append(car)
                                                #if car in the list, print messge
                                                print '\nCar sucesfully returned\n'
                                                #return menu option
                                                return self.option(self.menu_o()) 
                                        #while loop will count how many cars checked and then alst car checked if reg not in the 
                                        #list it will print messege that car is not found in the list
                                        total = 0
                                        #whil list lenght is less than total
                                        while total <= len(self.rentet_electric_cars):
                                            #Count total
                                           total += 1
                                           #if total equal to lenght print messege that reg not in the list
                                           if total == len(self.rentet_electric_cars):
                                               print '\nNo car in the return list with this registration number, pelase try again'
                                    else:
                                        print '\nThis customer is not found in our database, pelase try again'
                                            
                            #if customer want to return diesel car
                            elif question == 'd':
                                #if lenght of rentet cars equal or less than 0
                                if len(self.rentet_diesel_cars) <= 0:
                                    #error messege is printed
                                    print '\nNo diesel cars are rentet'
                                else:
                                    #cutomers cridentials
                                    cust = raw_input('Please enter your email address: ')
                                    if cust in self.customers:
                                        #print all cars which are in rented cars dictionary and rented by this customer
                                        self.nice_display (self.rentet_diesel_cars, cust)
                                        #insert registration number
                                        reg = raw_input('Please enter the reg: ')
                                        #check each car in rented cars list
                                        for car in self.rentet_diesel_cars:
                                            #if reg in rented cars list
                                            if reg.lower() == car['car'].getReg().lower():
                                                #remove from the rented cars list
                                                self.rentet_diesel_cars.remove(car)
                                                #add back to the cars list
                                                self.diesel_cars.append(car)
                                                #if car in the dictionary, print messge
                                                print '\nCar sucesfully returned\n'
                                                return self.option(self.menu_o()) 
                                        #while loop will count how many cars checked and then alst car checked if reg not in the 
                                        #list it will print messege that car is not found in the list
                                        total = 0
                                        #whil list lenght is less than total
                                        while total <= len(self.rentet_diesel_cars):
                                            #Count total
                                           total += 1
                                           #if total equal to lenght print messege that reg not in the list
                                           if total == len(self.rentet_diesel_cars):
                                               print '\nNo car in the return list with this registration number, pelase try again'
                                    else:
                                        print '\nThis customer is not found in our database, pelase try again'
                            elif question == 'h':
                                #if lenght of rentet cars equal or less than 0
                                if len(self.rentet_hybrid_cars) <= 0:
                                    #error messege is printed
                                    print '\nNo hybrid cars are rentet'
                                else:
                                    #cutomers cridentials
                                    cust = raw_input('Please enter your email address: ')
                                    if cust in self.customers:
                                        #print all cars which are in rented cars list
                                        self.nice_display (self.rentet_hybrid_cars, cust)
                                        #insert registration number
                                        reg = raw_input('Please enter the reg: ')
                                        #check each car in rented cars list
                                        for car in self.rentet_hybrid_cars:
                                            #if reg in rented cars list
                                            if reg.lower() == car['car'].getReg().lower():
                                                #remove from the rented cars list
                                                self.rentet_hybrid_cars.remove(car)
                                                #add back to the cars dictioanry
                                                self.hybrid_cars.append(car)
                                                #if car in the dictionary, print message
                                                print '\nCar sucesfully returned\n'
                                                return self.option(self.menu_o()) 
                                        #while loop will count how many cars checked and then alst car checked if reg not in the 
                                        #list it will print messege that car is not found in the list
                                        total = 0
                                        #whil list lenght is less than total
                                        while total <= len(self.rentet_hybrid_cars):
                                            #Count total
                                           total += 1
                                           #if total equal to lenght print messege that reg not in the list
                                           if total == len(self.rentet_hybrid_cars):
                                               print '\nNo car in the return list with this registration number, pelase try again'
                                    else:
                                        print '\nThis customer is not found in our database, pelase try again'
                            elif question == 'b':
                                return self.option(self.menu_o())
                            elif question == 'q':
                                print '\nYou just quit a rental App'
                                return 'done'
                            #else print wrong input
                            else:
                                print '\nWrong input'
                        except:
                            print question
                    elif question == 'n':
                        #if user enter n program ecits
                        print '\nThank you for using our rental sevices'
                        return 'done'
                    #add option to return if he wants to return to rent or return
                except:
                    print 'Please enter y/n'
    
    #create function to output file            
    def output_file (self):
            question = ''
            while done(question):
                #ask if user would like to rent a car
                question = raw_input('Would you like to output file? \n\
\nY - Yes\n\
N - No\n\
\nPlease enter your option: ')
                question = question.lower()
                try:
                    #if answer is yes
                    if question == 'y':
                        #ask what type of car he want to rent
                        question = raw_input('What file you would like to output?\n\
\n1 - Available petrol cars\n\
2 - Rentet petrol cars\n\
3 - Available electric cars\n\
4 - Rentet electric cars\n\
5 - Available diesel cars\n\
6 - Rentet diesel cars\n\
7 - Available hybrid cars\n\
8 - Rentet hybrid cars\n\
B - Back to MENU\n\
Q - To Quit\n\
\nPlease enter your option: ')
                        question = question.lower()
                        try:
                            #is user select 1
                            if question == '1':
                                #output available petrol cars in txt format
                                output_handler = open('Available petrol cars.txt', 'w')
                                for car in self.petrol_cars:
                                    output_handler.write(str(car))
                                #close file handler
                                output_handler.close()
                                #return menu option
                                return self.option(self.menu_o())
                            elif question == '2':
                                #output rentet petrol cars in txt format
                                output_handler = open('Rentet petrol cars.txt', 'w')
                                for car in self.rentet_petrol_cars:
                                    output_handler.write(str(car))
                                #close file handler
                                output_handler.close()
                                #return menu option
                                return self.option(self.menu_o())
                            elif question == '3':
                                #output available electric cars in txt format
                                output_handler = open('Available electric cars.txt', 'w')
                                for car in self.electric_cars:
                                    output_handler.write(str(car))
                                #close file handler
                                output_handler.close()
                                #return menu option
                                return self.option(self.menu_o())
                            elif question == '4':
                                #output rentet electric cars in txt format
                                output_handler = open('Rentet electric cars.txt', 'w')
                                for car in self.rentet_electric_cars:
                                    output_handler.write(str(car))
                                #close file handler
                                output_handler.close()
                                #return menu option
                                return self.option(self.menu_o())
                            elif question == '5':
                                #output available diesel cars in txt format
                                output_handler = open('Available diesel cars.txt', 'w')
                                for car in self.diesel_cars:
                                    output_handler.write(str(car))
                                #close file handler
                                output_handler.close()
                                #return menu option
                                return self.option(self.menu_o())
                            elif question == '6':
                                #output rentet electric cars in txt format
                                output_handler = open('Rentet diesel cars.txt', 'w')
                                for car in self.rentet_diesel_cars:
                                    output_handler.write(str(car))
                                #close file handler
                                output_handler.close()
                                #return menu option
                                return self.option(self.menu_o())
                            elif question == '7':
                                #output available hybrid cars in txt format
                                output_handler = open('Available hybrid cars.txt', 'w')
                                for car in self.hybrid_cars:
                                    output_handler.write(str(car))
                                #close file handler
                                output_handler.close()
                                #return menu option
                                return self.option(self.menu_o())
                            elif question == '8':
                                #output rentet hybrid cars in txt format
                                output_handler = open('Rentet hybrid cars.txt', 'w')
                                for car in self.rentet_hybrid_cars:
                                    output_handler.write(str(car))
                                #close file handler
                                output_handler.close()
                                #return menu option
                                return self.option(self.menu_o())
                            #insert q to quit
                            elif question == 'b':
                                return self.option(self.menu_o())
                            elif question == 'q':
                                print '\nYou just quit a rental App'
                                return 'done'
                            #else print wrong input
                            else:
                                print '\nWrong input'
                        except:
                            print question
                    elif question == 'n':
                        #if user enter n program exits
                        print '\nThank you for using our rental sevices'
                        return 'done'
                    #asdd option to return back to the menu
                except:
                    print 'Please enter y/n'
           
                    
    def option(self, menu_o):
        if menu_o == 1:
             self.process_rental()
        elif menu_o == 2:
            self.process_return()
        elif menu_o == 3:
            self.output_file()


                            
                    

#assigne class
dealership = Dealership()
#assigne file to the variable cars_file
cars_file = open ('cars.csv')
#create stock of the cars
dealership.create_stock(cars_file)   
#call dealership option function to runn the app
dealership.option(dealership.menu_o())     
