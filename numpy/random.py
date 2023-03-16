import numpy as np
from numpy import random

print("Randint")
x = random.randint(7) # give random integer in which are < 7
print(x)
print("--------------------")

print("Rand")
y = random.rand(10) # give random ten floats 
print(y)
print("--------------------")

print("size") # shape of array and size as parameter is optional

z = random.randint(7, size=(1, 2)) # give random integer 2D array including 1 sub-array with 2 elements
print(z)
print("--------------------")

print("choice")
arr = np.array([2, 4, 6, 8])
arr_c = random.choice(arr, size = (1,2)) # give random 2D array with elements from 'arr' i.e[2, 4, 6, 8] 
print(arr_c)

print("--------------------")
print("Random Permutation")
print("shuffle")
arr_shuffle = random.shuffle([1, 2, 3, 4]) # shuffle modify the original array
print(arr_shuffle)

print("permutation")
arr_per = random.permutation([1, 2, 3, 4]) # permutation don't modify the original array
print(arr_per)

