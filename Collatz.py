# Author Ricardo Rodrigues
  
# Defining the function 
def collatz(number):

 # If the number is negative print "Unfortunately this is not a positive Integer."
 if number <= 0:
       print("Unfortunately this is not a positive Integer.") 
       quit() 
       
# looping through and if number found is even divide it by 2
 elif number % 2 == 0:
        print(number // 2)
        return number // 2

 elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
       
# Type the number
n = input("Type a number: ")

# running the function togethe final result number 1
while n != 1:
    n = collatz(int(n))


# Reference:
# https://stackoverflow.com/questions/45990261/implementing-the-collatz-function-using-python
# Used lecture
