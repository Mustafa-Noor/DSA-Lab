import random
# function to make a random array
def RandomArray(size):
    randomNumbers = []
    for i in range(0,size):
        rand  = random.randint(0, 1000)
        randomNumbers.append(rand)
    return randomNumbers


# function to shuffle an array
def ShuffleArray(array, start, end):
    for i in range(end, start-1, -1):
        j = random.randint(0, end)

        # swap the values in i and j
        array[i], array[j] = array[j], array[i]


