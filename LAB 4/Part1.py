def Quicksort(A, p, r):
    if p < r:
        q = Partitions(A, p , r)
        Quicksort(A, p, q-1)
        Quicksort(A, q+1, r)


def Partitions(A, p, r):
    pivot = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= pivot:
            i = i+1
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[r] = A[r], A[i+1]

    return i+1
            

array = [12, 4, 5, 6, 7, 3, 1, 15]
Quicksort(array, 0, 7)
print(array)