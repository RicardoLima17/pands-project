# Author: Ricardo Rodrigues 
# This program reads in a large text file and outputs the number of "e"s it contains 
# This programme will find the character has 116960, We find "e"


# import collection to use Counter
import collections
filename = "moby-dick.txt"
# open file to read
with open (filename, "r") as info:
    # this line count all characteres 
    count = collections.Counter(info.read())
        # variable to store count
    value = (count)
# print all counter in value
print(value)
   
# Now we know "e" has 116960
N = 0
# open file to read
with open (filename, "r") as info:
    # new line 
    for line in info:
        # split variable line and store in new variable words
        words = line.split()
        # words store in new variable i
        for i in words:
            # create a new variable letter
            for letter in i:
                # letter "e"
                if letter == "e":
                    # count n = 0 and count once n + 1 if you use N + 2 count twice "e"
                    N = N + 1
# print "e" = 116960                
print (N)

# References:
#https://www.pythontutorial.net/python-basics/python-read-text-file/
#https://www.w3schools.com/python/python_file_open.asp
#https://www.sanfoundry.com/python-program-read-file-counts-number/
# Used lecture
