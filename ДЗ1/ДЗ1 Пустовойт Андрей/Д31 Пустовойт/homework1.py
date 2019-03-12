from random import randint  
import numpy as np


class RandomMatrix_5x5():
    def __init__(self):
        self.matrix = [[randint(-10, 10) for j in range(5)] for i in range(5)]

    def __str__(self):
        # this function by recursive call makes strings from arrays
        def to_string(lst):
            return str(lst[0]) + ',\n' + to_string(lst[1:]) if len(lst) > 1 else str(lst[0])
        return '[' + to_string(self.matrix) + ']'

    def write_to_file(self, file_name):
        with open(file_name, 'w') as file:
            file.write(str(self))

    def read_from_file(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
        mtrx = RandomMatrix_5x5()
        mtrx.matrix = [list(map(int, line.strip('[],\n').split(', '))) for line in lines]
        return mtrx

    def __mul__(self, other):
        other_data = other.matrix
        mtrx = RandomMatrix_5x5()   
        for i in range(5):
            for j in range(5):
              # cleaning matrix from random data
              mtrx.matrix[i][j] = 0
              for k in range(5):
                  mtrx.matrix[i][j] += self.matrix[i][k] * other_data[k][j]
        return mtrx

      
m1 = RandomMatrix_5x5()
m2 = RandomMatrix_5x5()
print(m1, '\n')
print(m2, '\n')

m1.write_to_file('m1.txt')
m3 = RandomMatrix_5x5.read_from_file('m1.txt')
print(m3, '\n')

m2.write_to_file('m2.txt')
m4 = RandomMatrix_5x5.read_from_file('m2.txt')
print(m4, '\n')
   
print('============== TESTING MULTIPLICATION ==============')
print(m3, '*', m4, '=', m3 * m4, sep='\n') 
print('============== RESULT FROM NUMPY ==============')
m5 = np.array([np.array(i) for i in m1.matrix])
m6 = np.array([np.array(i) for i in m2.matrix])
print(m5, '*', m6, '=', np.dot(m5, m6), sep='\n')