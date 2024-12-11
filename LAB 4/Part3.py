def CountingSort(arr):
    max_val = max(arr)
    min_val = min(arr)
    
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)
    
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    for i in range(len(arr)):
        arr[i] = output[i]

# Drivers Code
arr = [-5, -10, 0, -3, 8, 5, -1, 10]
CountingSort(arr)
print("Sorted array using Counting Sort:", arr)


#--------------------------------------------

def CountingSortRadix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    for i in range(n):
        arr[i] = output[i]

def RadixSort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        CountingSortRadix(arr, exp)
        exp *= 10


# Drivers Code
arr = [110, 45, 65, 50, 90, 602, 24, 2, 66]
RadixSort(arr)
print("Sorted array using Radix Sort:", arr)


#------------------------------------------------

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def BucketSort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]
    
    for num in arr:
        index = int(num * n)
        buckets[index].append(num)
    
    for bucket in buckets:
        InsertionSort(bucket)
    
    sortedArr = []
    for bucket in buckets:
        sortedArr.extend(bucket)
    
    return sortedArr


# Drivers Code

arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
sorted_arr = BucketSort(arr)
print("Sorted array using Bucket Sort:", sorted_arr)


#----------------------------------------------------------github