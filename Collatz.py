# Author Ricardo Rodrigues
       
def collatz(number):

 if number <= 0:
       print("Unfortunately this is not a positive Integer.") 
       quit() 

 elif number % 2 == 0:
        print(number // 2)
        return number // 2

 elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = input("Type a number: ")
while n != 1:
    n = collatz(int(n))


# Reference:
# https://stackoverflow.com/questions/45990261/implementing-the-collatz-function-using-python
# Used lecture
