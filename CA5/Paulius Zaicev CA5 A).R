#Function whicch returns addition
addition <- function(numb1, numb2) {
  return(numb1 + numb2)
}

#test addition function
#addition(1.5, 6.9)

#subtraction function
subtraction <- function(numb1, numb2) {
  return(numb1 - numb2)
}

#test subtraction function
#subtraction(1.9, 1.8)

dividion <- function(numb1, numb2){
  return(numb1 / numb2)
}

#test dividion
#dividion( 0, 2)
#dividion( 4, 2)
#dividion( 2, 0)
#dividion( 2.5, 2)

#multiplication
multiply <- function(numb1, numb2){
  return(numb1 * numb2)
}

#test multiplication
#multiply( 0, 2)
#multiply( 4, 2)
#multiply( 2, 0)
#multiply( 2.5, 2)

#first value to the power of the second value
#exponential
exponential <- function(numb1, numb2){
  return(numb1 ** numb2)
}


#test exponential
#exponential( 0, 2)
#exponential( 4, 2)
#exponential( 2, 0)
#exponential( 2.5, 2)
#exponential(-2,5)


#cubic value
cube <- function(numb1){
  return(numb1 ** 3)
}


#test exponential
#cube( 0)
#cube( 4)
#cube( 2)
#cube( 2.5)

#ten to power
ten_to_power <- function(numb1){
  return(10 ** numb1)
}


#test ten to power of insertet number
#ten_to_power( 0)
#ten_to_power( 4)
#ten_to_power( -2)
#ten_to_power( 2.5)


#square root
sqrt_func <- function(numb1){
    return(sqrt(numb1))
}


#test sqrt
#sqrt_func( 0)
#sqrt_func( 4)
#sqrt_func( -2)
#sqrt_func( 2.5)


#cubicroot function

cbroot <- function(numb1) {
  if(x < 0){
    return (- (-numb1)**(1/3))}
  else{
    return (numb1**(1/3))}}

#test cubic root function
#cbroot(-8)
#cbroot(8)
#cbroot(0)
#cbroot(-1.5)


#function to muliply first value by the 10 power to the second value (x * 10**y)
first_to_second <- function (numb1, numb2){
  return (numb1 * (10^numb2))
}

#tets first_to)second function
#first_to_second (10,10)
#first_to_second (10,-10)
#first_to_second (-10,10)
#first_to_second (0,10)
#first_to_second (10,0)

#In case to run interactive part functions must be executed each time


menu <- cat(paste("Please select below:",
        "1 - to add two numbers",
         "2 - to subtract",
         "3 - to divide",
         "4 - to multiply",
         "5 - first value to the power of the second value",
         "6 - cubic value of the number",
         "7 - ten to power of inserted number",
         "8 - square root",
         "9 - cubic root",
         "10 - muliply first value by the 10 power to the second value (x * 10**y)", sep = "\n"))


#user must insert menu option


#request user to select an option from the menu
input <- readline("Please enter a menu option:")
#covert to numeric
input <- as.numeric(input)


#if menu option -- 1 call addition function
if (input == 1) {
  #request to insert 1st number
  Numb1 <- readline("Please enter number 1:")
  #covert to numeric
  Numb1Numeric <- as.numeric(Numb1)
  #raw input as a string for a second number
  Numb2 <- readline("Please enter number 2:")
  #covert to numeric
  Numb2Numeric <- as.numeric(Numb2)
  addition <- addition(Numb1Numeric,Numb2Numeric)
  #sprintf - print stirng as a float, %2 decimal points
  additionString <- sprintf("%.2f", addition)
  message <- paste("The addition result is", additionString, sep=" ")
  print (message)
  
  #if menu selected options is equal 2, execute subtraction fucntion
} else if (input == 2){
  #request to insert 1st number
  Numb1 <- readline("Please enter number 1:")
  #covert to numeric
  Numb1Numeric <- as.numeric(Numb1)
  #raw input as a string for a second number
  Numb2 <- readline("Please enter number 2:")
  #covert to numeric
  Numb2Numeric <- as.numeric(Numb2)
  subtraction <- subtraction(Numb1Numeric,Numb2Numeric)
  #sprintf - print stirng as a float, %2 decimal points
  subtractionString <- sprintf("%.2f", subtraction)
  message <- paste("The subtraction result is", subtractionString, sep=" ")
  print (message)
  
  #if menu selected options is equal 3, execute dividion fucntion
} else if (input == 3){
  #request to insert 1st number
  Numb1 <- readline("Please enter number 1:")
  #covert to numeric
  Numb1Numeric <- as.numeric(Numb1)
  #raw input as a string for a second number
  Numb2 <- readline("Please enter number 2:")
  #covert to numeric
  Numb2Numeric <- as.numeric(Numb2)
  dividion <- dividion(Numb1Numeric,Numb2Numeric)
  #sprintf - print stirng as a float, %2 decimal points
  dividionString <- sprintf("%.2f", dividion)
  message <- paste("The dividion result is", dividionString, sep=" ")
  print (message)
  
  #if menu selected options is equal 4, execute multiply fucntion
} else if (input == 4){
  #request to insert 1st number
  Numb1 <- readline("Please enter number 1:")
  #covert to numeric
  Numb1Numeric <- as.numeric(Numb1)
  #raw input as a string for a second number
  Numb2 <- readline("Please enter number 2:")
  #covert to numeric
  Numb2Numeric <- as.numeric(Numb2)
  multiply <- multiply(Numb1Numeric,Numb2Numeric)
  #sprintf - print stirng as a float, %2 decimal points
  multiplyString <- sprintf("%.2f", multiply)
  message <- paste("The multiplication result is", multiplyString, sep=" ")
  print (message)
  
  #if menu selected options is equal 5, execute exponential fucntion
} else if (input == 5){
  #request to insert 1st number
  Numb1 <- readline("Please enter number 1:")
  #covert to numeric
  Numb1Numeric <- as.numeric(Numb1)
  #raw input as a string for a second number
  Numb2 <- readline("Please enter number 2:")
  #covert to numeric
  Numb2Numeric <- as.numeric(Numb2)
  exponential <- exponential(Numb1Numeric,Numb2Numeric)
  #sprintf - print stirng as a float, %2 decimal points
  exponentialString <- sprintf("%.2f", exponential)
  message <- paste("The exponential result is", exponentialString, sep=" ")
  print (message)
  
  #if menu selected options is equal 6, execute cubic fucntion
} else if (input == 6){
  #request to insert 1st number
  Numb1 <- readline("Please enter a number:")
  #covert to numeric
  Numb1Numeric <- as.numeric(Numb1)
  cubic <- cube(Numb1Numeric)
  #sprintf - print stirng as a float, %2 decimal points
  cubicString <- sprintf("%.2f", cubic)
  message <- paste("The cube result is", cubicString, sep=" ")
  print (message)

  #if menu selected options is equal 7, execute ten to power fucntion 
  #which will evaluete first number to power of the scond number
} else if (input == 7){
  #request to insert 1st number
  Numb1 <- readline("Please enter a number:")
  #covert to numeric
  Numb1Numeric <- as.numeric(Numb1)
  ten_to_power <- ten_to_power(Numb1Numeric)
  #sprintf - print stirng as a float, %2 decimal points
  ten_to_powerString <- sprintf("%.2f", ten_to_power)
  message <- paste("Ten to power of inserted numberis", ten_to_powerString, sep=" ")
  print (message)

  #if menu selected options is equal 8, execute square root function 
} else if (input == 8){
  #request to insert number
  Numb1 <- readline("Please enter a number:")
  #covert to numeric
  Numb1Numeric <- as.numeric(Numb1)
  sqrt_func <- sqrt_func(Numb1Numeric)
  #sprintf - print stirng as a float, %2 decimal points
  sqrt_funcString <- sprintf("%.2f", sqrt_func)
  message <- paste("The square root of inserted number is", sqrt_funcString, sep=" ")
  print (message)

  #if menu selected options is equal 9, execute cubic root function 
} else if (input == 9){
  #request to insert number
  Numb1 <- readline("Please enter a number:")
  #covert to numeric
  Numb1Numeric <- as.numeric(Numb1)
  cbroot <- cbroot(Numb1Numeric)
  #sprintf - print stirng as a float, %2 decimal points
  cbrootString <- sprintf("%.2f", cbroot)
  message <- paste("The cubic root of inserted number is", cbrootString, sep=" ")
  print (message)

  #if menu selected options is equal 10, execute first to second function
} else if (input == 10){
  #request to insert 1st number
  Numb1 <- readline("Please enter number 1:")
  #covert to numeric
  Numb1Numeric <- as.numeric(Numb1)
  #raw input as a string for a second number
  Numb2 <- readline("Please enter number 2:")
  #covert to numeric
  Numb2Numeric <- as.numeric(Numb2)
  first_to_second <- first_to_second(Numb1Numeric,Numb2Numeric)
  #sprintf - print stirng as a float, %2 decimal points
  first_to_secondString <- sprintf("%.2f", first_to_second)
  message <- paste("The result for muliplying first value by the 10 to power to the second value (x * 10**y) is", first_to_secondString, sep=" ")
  print (message)
} else {
    print ('Out of menu range')
  }

  



