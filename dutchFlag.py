from algorithm import sortArray
from generate import generateRandomArray
import time

#INPUT
lengthOfArray = int(input("Please enter how long you want the array to be: "))
print("\nHere's your array: ")

#Generates Random Unsorted Array
flag = generateRandomArray(lengthOfArray)
print(flag)
time.sleep(2)
#Sorts Arrays
print("And now to sort it! ")
time.sleep(1)
sortArray(flag)

#Declares it Sorted
print("SORTED!!!")
