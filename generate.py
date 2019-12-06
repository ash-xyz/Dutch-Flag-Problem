from random import shuffle

#Generates an unsorted array of equal 1, 2 & 3's
def generateRandomArray(length):
    list = [1 for i in range(0, 3*length)]
    for i in range(length, 2*length):
        list[i] = 2
    for j in range(2*length, 3*length):
        list[j] = 3
    shuffle(list)
    return list