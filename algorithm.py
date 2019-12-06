import time

#Algorithmic Approach to sorting the array in O(n)

#Basic swapping function for Lists
def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

#Sorts the Array
def sortArray(list):
    i = 0
    j = 0
    k = len(list)
    while(j < k):
        if list[j] == 1:
            swapPositions(list, i, j)
            i += 1
            j += 1
        elif list[j] == 2:
            j += 1
        elif(list[j] == 3):
            swapPositions(list, j, k-1)
            k -= 1
        print(list)
        time.sleep(0.2)
        print('\n')