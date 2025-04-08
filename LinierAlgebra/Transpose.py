
# Sum matrix
def matrix_sum(a,b):
    return

# Multiply matrix
# Notation C[i],[j] = sum A[i],[k] . B[k],[j]
def matrix_multiply(a,b):

    if (len(a[0]) != len(b)): # Rules of matrix multiply K = K dimana K adalah jumlah kolom matrix pertama dan baris matrix kedua ( m x n ) (n x o)
        return None
    
    row = len(a)
    col = len(b[0])
    index = len(b) 
    
    result = [[0 for _ in range(col)] for _ in range(row)]

    # Perkalian Matriks
    for i in range(row):
        for j in range(col):
            total = 0
            for k in range(index):
                total += a[i][k] * b[k][j]
            result[i][j] = total

    return result

# notation : At(i,j) = A(j,i)
# transpose with memory
def matrix_transpose(a):
    result = [[0 for _ in range(len(a))] for _ in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[i])):
            result[j][i] = a[i][j]
    return result

# Example
matrix_a = [
    [2, 1],
    [6, 5],
    [8, 9]
]

matrix_b = [
    [2, 1, 3],
    [6, 5, 3]
]


print(matrix_multiply(matrix_a, matrix_b))


def inverse_matrix(a, b):
    return None