# 4) Write a Python program to perform matrix multiplication using lists of lists

def matrix_multiplication(matrix1, matrix2):
 
    if len(matrix1[0]) != len(matrix2):
        print("Matrices cannot be multiplied. Inner dimensions do not match.")
        return None

   
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

   
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[7, 8],
           [9, 10],
           [11, 12]]

product = matrix_multiplication(matrix1, matrix2)
if product:
    print("Result of matrix multiplication:")
    for row in product:
        print(row)
