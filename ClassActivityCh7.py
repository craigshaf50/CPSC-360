# ClassActivityCh7_2/13/23
#
# pt1: checking matrix operations in python
# pt2: function from 7.2.2.1

import numpy as np

# pt1: Matrix order of operations
# defining two matrices
matrix1 = np.array([[10, 20], [15, 25]])
matrix2 = np.array([[20, 30], [25, 35]])

# np.add() adds matrices
print("Addition of the two matrices: ")
print(np.add(matrix1, matrix2))

# np.subtract() subtracts matrices
print("Subtraction of the two matrices: ")
print(np.subtract(matrix1, matrix2))

# np.divide() divides matrices
print("Division of matrix1 by matrix2: ")
print(np.divide(matrix1, matrix2))

# np.multiply() multiplies matrices
print("Multiplication of the two matrices: ")
print(np.multiply(matrix1, matrix2))

# testing order of operations
print('m1 / (m1-m2) = ')
print(np.divide(matrix1, np.subtract(matrix1, matrix2)))

print('(m1*m2) + (m1-m2) = ')
print(np.add(np.multiply(matrix1, matrix2), np.subtract(matrix1, matrix2)))


# pt2: Evaluates the function from section 7.2.2
a = 10
def fun(value):
    global a
    a = 20
    return value

b = a + fun(a)
print('the value of b is: ', b)
# prints 20 because it gets the value of a (10) first before calling the function that makes a = 20.
# therefore, a + fun(a) = 10 + 10 = 20.