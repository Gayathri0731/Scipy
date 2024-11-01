#  Linear Algebra

import numpy as np 
import scipy.linalg as Linalg

#  the equation mannual (2D)
#  3x + 4y = 10
#  2x + 5y = 9

a = np.array ([
    [3,4],[2,5]
])
b = np.array([10,9])
print("Solution :",Linalg.solve(a,b))
print()

array = ([
    [1,2,3],
    [4,5,6],
    [8,8,9]
])
print("Numpy array :")
print(array)
print()

#  Determinant 
determinant = Linalg.det(array)
print("Determinant :",determinant)
print()

#  Find Matrix inverse
inv_arr = Linalg.inv(array)
print("Inverse Array : \n",inv_arr)
print()
print("Matrix-inverse Product :")
print(array@inv_arr)
print()

# Obtaining Eigen values and Eigen Vectors 
array2 = np.array([[1,-2,0],[-2,1,0],[0,0,3]])
eg_val , eg_vec = Linalg.eig(array2)
print("Eigen Values :",eg_val)
print()
print("Eigen Vectors :\n",eg_vec)
print()

# Singular value decomposition
#  array = PD (P_inverse)
#  P-->eigen_vector , D-->Diagnol_Value
P = eg_vec
P_inv = Linalg.inv(eg_vec)

D = []
for index, eg_val in enumerate(eg_val):
    row = np.zeros((3))
    row[index]= eg_val
    D.append(row)
D = np.array(D)
print("Singular Value Decomposition :\n",P @ D @ P_inv)
print()