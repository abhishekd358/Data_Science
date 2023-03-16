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

print("--------------------")
print("Data Distribution")
print("of ",arr,"is")
data_dist = random.choice(arr, p=[0.2, 0.4, 0.3, 0.1], size=(1, 2))
print(data_dist)


print("--------------------")
print("importing matplotlib")
import matplotlib.pyplot as plt

print("importing Seaborn")
import seaborn as sns
sns.distplot([3, 5, 7, 11], hist= True) # hist is histogram
#plt.show()   # remove comment to show graph

'''from here if you want to see graph of distributions use above code block'''
print("--------------------")
print("Normal Distribution")
arr_normal = random.normal(loc= 7, scale= 2, size=(1, 2)) # loc- Mean, scale- Standard Deviation, size- shape of array you want
print(arr_normal)
sns.distplot(arr_normal)
#plt.show()  # remove comment to show graph

print("--------------------")
print("Binomial Distribution")
arr_binomial = random.binomial(n= 2, p=[0.2, 0.8]) # n- number of trials, p- Probability(sum must be eqaul to 1), size- shape of array
print(arr_binomial)
sns.distplot(arr_binomial)
#plt.show()  # remove comment to show graph

print("--------------------")
print("Poisson Distribution")

arr_poisson = random.poisson(lam= 2,size=(3, 2)) # lam- rate or unknown number of occurence, size- shape of array
print(arr_poisson)
sns.distplot(arr_poisson)
#plt.show()  # remove comment to show graph

