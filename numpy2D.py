import numpy as np
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],[65.4, 59.2, 63.6, 88.4, 68.7]])
print (np_2d)
print (np_2d.shape)

def index():
    print (np_2d[0]) #row
    print (np_2d[0][2])
    print (np_2d[0,2])
    print (np_2d[:,1:3]) #output = 2d array with 2 rows and 2 cols
    print (np_2d[1,:]) #1st col
           

index()
