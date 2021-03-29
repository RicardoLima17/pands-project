# Author Ricardo Rodrigues

import datetime

# check the day of today to run the programme
dayOfweek =datetime.datetime.today().weekday()
# print the date today 
print (dayOfweek)

# if the date is monday
if dayOfweek == 0: # you can use @if dayOfweek == monday:
# print this message below
    print ("Yes, unfortunately today is a weekday.")

# if the date is tuesday
elif dayOfweek == 1: # you can use @if dayOfweek == tuesday:
# print this message below    
    print ("Yes, unfortunately today is a weekday.")

# if the date is wednesday
elif dayOfweek == 2: # you can use @if dayOfweek == wednesday:
# print this message below    
    print ("Yes, unfortunately today is a weekday.")

# if the date is thursday
elif dayOfweek == 3: # you can use @if dayOfweek == thursday:
# print this message below    
    print ("Yes, unfortunately today is a weekday.")

# if the date is friday
elif dayOfweek == 4: # you can use @if dayOfweek == friday:
# print this message below    
    print ("Yes, unfortunately today is a weekday.")
       
else:
# if is not 0 = monday, 1 = tuesday, 3 = wednesday, 4 = thursday or 5 = friday    
# print satuday and sunday    
    print("It is the weekend, yay!")    

    
# References
# https://www.w3schools.com/python/python_datetime.asp
# Used lecture on Tuesday program as a base for the problem.
