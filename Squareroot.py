# Author Ricardo

# variable number with input a positive number 
number = float(input("Please enter a positive number: "))

# conditional if bigger than 0 go ahead if not closed the programme
if number <= 0.0:
    print("Unfortunately this is not a positive number.") 
    quit()

# variables to use in your formula
a = 1/2
b = 5

# first calculation with variables
cal1 = a*(number/b+b)

# second calculation with variables
cal2 = a*(number/cal1+cal1)

# last calculation with variables
cal3 = a*(number/cal2+cal2)

# print first calculation with round 1 decimal
print (round(cal1, 1))

# print second calculation with round 1 decimal
print (round(cal2, 1))

## print the final calculation
print ("The square root of {} is approx. {}." .format(number, (round(cal3, 1,))))

# References:
#https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD_fZWj7Tcs
# Used lecture
