from funcs import ShuffleArray
from Insertion import InsertionSort
from MergeSort import MergeSort
import time

# read the words from words.txt
def ReadWords():
    wordsFile = open(file='words.txt', mode='r')
    lines = wordsFile.read()
    wordsArray = []
    words = lines.split()
    for w in words:
        word = w
        wordsArray.append(word)
    return wordsArray

# function to calculate the runtime of sorting functions
def CalculateRuntime(sortFunction, myArray, start, end):
    start_time = time.time()
    sortFunction(myArray, start, end)
    end_time = time.time()
    runtime = end_time - start_time 
    return runtime


wordsArray = ReadWords()
end = len(wordsArray)-1

# insertion sort time before shuffling
arrayCopy = wordsArray.copy()
insertionTime = CalculateRuntime(InsertionSort, arrayCopy, 0, end)
print("The runtime of insertion sort before shuffling: ", insertionTime)

# merge sort time before shuffling
arrayCopy = wordsArray.copy()
mergeSortTime = CalculateRuntime(MergeSort, arrayCopy, 0, end)
print("The runtime of merge sort before shuffling: ", mergeSortTime)



# shuffling the array
ShuffleArray(wordsArray, 0, end)

# insertion sort time after shuffling
arrayCopy = wordsArray.copy()
shuffledInsertionTime = CalculateRuntime(InsertionSort, arrayCopy, 0, end)
print("The runtime of insertion sort after shuffling: ", insertionTime)

# merge sort time after shuffling
arrayCopy = wordsArray.copy()
shuffledMergeSortTime = CalculateRuntime(MergeSort, arrayCopy, 0, end)
print("The runtime of merge sort after shuffling: ", mergeSortTime)

# compare times
if shuffledInsertionTime > insertionTime:
    print("Insertion Sort took longer after shuffling.")
else:
    print("Insertion Sort was faster after shuffling.")

if shuffledMergeSortTime > mergeSortTime:
    print("Merge Sort took longer after shuffling.")
else:
    print("Merge Sort was faster after shuffling.")


