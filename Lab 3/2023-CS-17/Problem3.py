
#1. ----------------------------------------------
def printMatrix(A, starting_index, rows, columns):
    startRow, startCol = starting_index
    totalRows = len(A)
    totalColumns = len(A[0])
    for i in range(startRow, startRow+rows):
        if(i < totalRows):
            for j in range(startCol, startCol+columns):
                if(j < totalColumns):
                    print(A[i][j], end=" ")
            print()

# Driver Code
A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

starting_index = (4, 3)
rows = 2
columns = 2

printMatrix(A, starting_index, rows, columns)
#-------------------------------------------------------



#2. ----------------------------------------------
def MatAdd(A, B):
    rowsA = len(A)
    rowsB = len(B)
    colA = len(A[0])
    colB = len(B[0])

    resultantMatrix = []

    if rowsA != rowsB:
        print("Matrices have different no of rows")
        return None

    for i in range(rowsA):
        if len(A[i]) != len(B[i]):
            print("Matrices have different no of columns")
            return None

   
    for i in range(0, rowsA):
        arr = []
        for j in range(0, colA):
            sum = A[i][j] + B[i][j]
            arr.append(sum)
        resultantMatrix.append(arr)
    
    return resultantMatrix

# Example usage:
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = MatAdd(A, B)

# Printing the result
if result:
    for row in result:
        print(row)
#--------------------------------------------------------




#3 ----------------------------------------------
def MatAddPartial(A, B, start, size):
    startRow , startCol = start
    rowsA = len(A)
    rowsB = len(B)
    colA = len(A[0])
    colB = len(B[0])
    resMatrix = []

    for i in range(startRow, startRow+size):
        if(i < rowsA and i < colA):
            arr = []
            for j in range(startCol, startCol+size):
                if(j < colA and j < colB):
                    sum = A[i][j] + B[i][j]
                    arr.append(sum)
            resMatrix.append(arr)

    return resMatrix


# Example matrices
A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

B = [
    [5, 4, 3, 2, 1],
    [10, 9, 8, 7, 6],
    [15, 14, 13, 12, 11],
    [20, 19, 18, 17, 16],
    [25, 24, 23, 22, 21]
]

# Define the start position and the size of the submatrix
start = (1, 2)  # Starting from 2nd row and 3rd column
size  = 2   # 2 rows and 2 columns

# Call the function
result = MatAddPartial(A, B, start, size)

# Print the result
if result:
    print("Resultant Matrix:")
    for row in result:
        print(row)



# 4. -------------------------------------------
def MatMul(A, B):
    rowsA = len(A)
    rowsB = len(B)
    colA = len(A[0])
    colB = len(B[0])

    resMatrix = []

    if(colA == rowsB):
        resMatrix = [[0 for a in range(colB)] for b in range(rowsA)]
        for i in range(rowsA):
            for j in range(colB):
                for k in range(colA):
                    resMatrix[i][j] += A[i][k] * B[k][j]

    return resMatrix


# Example matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Call the function
result = MatMul(A, B)

# Print the result
if result:
    print("Resultant Matrix after multiplication:")
    for row in result:
        print(row)


#-------------------------------------------------

#6. ------------------------------------------------

def MatMulPartialRecursive(A, B, startA, startB, size):
    startRowA, startColA = startA
    startRowB, startColB = startB

    # Base case: 
    if size == 1:
        return [[A[startRowA][startColA] * B[startRowB][startColB]]]

    
    mid = size // 2

    
    C11 = MatAdd(
        MatMulPartialRecursive(A, B, (startRowA, startColA), (startRowB, startColB), mid),
        MatMulPartialRecursive(A, B, (startRowA, startColA + mid), (startRowB + mid, startColB), mid)
    )

    C12 = MatAdd(
        MatMulPartialRecursive(A, B, (startRowA, startColA), (startRowB, startColB + mid), mid),
        MatMulPartialRecursive(A, B, (startRowA, startColA + mid), (startRowB + mid, startColB + mid), mid)
    )

    C21 = MatAdd(
        MatMulPartialRecursive(A, B, (startRowA + mid, startColA), (startRowB, startColB), mid),
        MatMulPartialRecursive(A, B, (startRowA + mid, startColA + mid), (startRowB + mid, startColB), mid)
    )

    C22 = MatAdd(
        MatMulPartialRecursive(A, B, (startRowA + mid, startColA), (startRowB, startColB + mid), mid),
        MatMulPartialRecursive(A, B, (startRowA + mid, startColA + mid), (startRowB + mid, startColB + mid), mid)
    )

    # Combine the results into a single matrix
    result = []

    # Combine the top halves C11 and C12
    for i in range(mid):
        result.append(C11[i] + C12[i])

    # Combine the bottom halves C21 and C22
    for i in range(mid):
        result.append(C21[i] + C22[i])

    return result


    # Driver Code Example
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

B = [
    [16, 15, 14, 13],
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
]

startA = (0, 0)
startB = (0, 0)
size = 4   


result = MatMulPartialRecursive(A, B, startA, startB, size)

# Printing the result
if result:
    for row in result:
        print(row)

#---------------------------------------------------------------




#7.-------------------------------------------------------------
# Helper function to split a matrix into quarters
def MatSub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]
    
def splitMatrix(A):
    n = len(A)
    mid = n // 2
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    return A11, A12, A21, A22

# Helper function to join four matrices into one
def joinMatrix(C11, C12, C21, C22):
    n = len(C11) * 2
    C = [[0] * n for _ in range(n)]
    mid = n // 2
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    return C

# Strassen's Matrix Multiplication function
def MatMulStrassen(A, B):
    n = len(A)

    # Base case: 1x1 matrix multiplication
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Split A and B into 4 submatrices
    A11, A12, A21, A22 = splitMatrix(A)
    B11, B12, B21, B22 = splitMatrix(B)

    # Compute the 7 products (Strassen's formula)
    M1 = MatMulStrassen(MatAdd(A11, A22), MatAdd(B11, B22))
    M2 = MatMulStrassen(MatAdd(A21, A22), B11)
    M3 = MatMulStrassen(A11, MatSub(B12, B22))
    M4 = MatMulStrassen(A22, MatSub(B21, B11))
    M5 = MatMulStrassen(MatAdd(A11, A12), B22)
    M6 = MatMulStrassen(MatSub(A21, A11), MatAdd(B11, B12))
    M7 = MatMulStrassen(MatSub(A12, A22), MatAdd(B21, B22))

    # Compute the resulting submatrices
    C11 = MatAdd(MatSub(MatAdd(M1, M4), M5), M7)
    C12 = MatAdd(M3, M5)
    C21 = MatAdd(M2, M4)
    C22 = MatAdd(MatSub(MatAdd(M1, M3), M2), M6)

    # Combine the submatrices into one
    return joinMatrix(C11, C12, C21, C22)


# Example usage
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

B = [
    [16, 15, 14, 13],
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
]

# Call the function
result = MatMulStrassen(A, B)

# Print the result
if result:
    print("Resultant Matrix after Strassen's multiplication:")
    for row in result:
        print(row)
