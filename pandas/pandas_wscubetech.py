import pandas as pd

# creating series 1-Dimensional
arr = [2, 5, 3, 9]
x = pd.Series(arr)
print(x)
print(x[2])
print('-----------------------')
# indexing parameter 
print("indexing parameter")
var = pd.Series(arr, index= ['a', 'b', 'c', 'd'])
print(var)
print(var[2])
print('-----------------------')

# type changing parameter
print("type changing parameter")
tc = pd.Series(arr, index= ['a', 'b', 'c', 'd'], dtype='float')
print(tc)
print('-----------------------')

# name parameter
print("Name parameter")
Na = pd.Series(arr, index= ['a', 'b', 'c', 'd'], dtype='float', name='py')
print(Na)
print('-----------------------')

# passing dictionaries
print('passing Dictionaries')
dict = {
    'fruits' : ['pineapple','blueberry','apple'],
    'quantity' : [10, 4, 8]
}
out = pd.Series(dict) 
print(out) # data type is Object becuase data is mixed with string and int
print('-----------------------')

# seies with only one value
print('series with value one')
s = pd.Series(20, index=[11, 12, 13, 14, 15, 16])
print(s)

# pandas does not give BroadCast Error while Numpy give BroadCast Error
# BroadCasting
print('-----------------------')

print("adding with different number of elements")
s1 = pd.Series(20, index=[11, 12, 13, 14, 15, 16])
s2 = pd.Series(20, index=[11, 12, 13])
print(s1+s2) # output is Float type
print()
print()
