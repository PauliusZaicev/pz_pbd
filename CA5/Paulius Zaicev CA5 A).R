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

cbroot <- function(x) {
  if(x < 0){
    return (- (-x)**(1/3))}
  else{
    return (x**(1/3))}}

#test cubic root function
#cbroot(-8)
#cbroot(8)
#cbroot(0)
#cbroot(-1.5)

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
input <- readline("Please enter a menu option:")
#covert to numeric
input <- as.numeric(input)


if (input == 1) {
  Numb1 <- readline("Please enter number 1:")
  #covert to numeric
  Numb1Numeric <- as.numeric(Numb1)
  #raw input as a string
  Numb2 <- readline("Please enter number 2:")
  #covert to numeric
  Numb2Numeric <- as.numeric(Numb2)
  addition <- addition(Numb1Numeric,Numb2Numeric)
  #sprintf - print stirng as a float, %2 decimal points
  additionString <- sprintf("%.2f", addition)
  message <- paste("the result is", additionString, sep=" ")
  print (message)
} else if (input == 2){
  print('b is greater')
}

