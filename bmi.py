import numpy as np
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
'''Without NumPy:
BMI = weight/(height ** 2)
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
'''

'''With Numpy:'''
np_height = np.array(height)
#print (np_height)
np_weight = np.array(weight)
#print (np_weight)
bmi = np_weight/(np_height ** 2)
print (bmi)

#numpy operations
def add():
    print (weight + weight) #without numpy
    print (np_weight + np_weight)
def index():
    print (bmi[1]) #indexing still starts at 0
def inequality():
    print (bmi[bmi > 21.5])
def type():
    print(type(np_height)) #returns <class 'numpy.ndarray'>

