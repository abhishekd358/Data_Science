import numpy as np

# 1D array decalaration

print("1D array decalaration") 
d1_arr = np.array([1, 2, 3, 4, 5, 6])
print(d1_arr)

# 2D array decalaration 

print("2D array decalaration")
d2_arr = np.array([[1,2],[6,8],[4,7]])
print(d2_arr)

# 3D array declaration

print("3D array declaration")
d3_arr = np.array([[[12,14,6]]])
print(d3_arr)

# array indexing 

print("array indexing")
print(d1_arr[3])  
print(d2_arr[2, 1])
print(d3_arr[0])
print(d3_arr[0, 0])
print(d3_arr[0,0,2])

# array slicing 

print("array slicing")
print(d1_arr[0:3])


print(d2_arr[0])
print(d2_arr[0:2])
print(d2_arr[1, : ])
print(d2_arr[0:1, 0:2])
print(d2_arr[0:3, : ])


print(d3_arr[0, 0:2])

# checking dimensions of array

print("checking dimensions of array")
print(d1_arr.ndim)
print(d2_arr.ndim)
print(d3_arr.ndim)

# defining 1d array with different dimenstions

print("defining 1d array with different dimenstions")
d1 = np.array(d1_arr, ndmin= 2)
print(d1)
print(d1.ndim)

d2 = np.array(d2_arr, ndmin= 3)
print(d2)
print(d2.ndim)

d3 = np.array(d3_arr, ndmin= 6)
print(d3)
print(d3.ndim)

# checking data types of array

print(d1_arr.dtype)
print(d2_arr.dtype)
print(d3_arr.dtype)

# changing the data type of array

print(d1_arr.astype("f"))
print(d2_arr.astype("f"))
print(d3_arr.astype("f"))

# shape of array

print(d1_arr.shape)
print(d2_arr.shape)
print(d3_arr.shape)

# copy of array 

copy_d1_arr = d1_arr.copy
print(copy_d1_arr)  # gives memory location
copy_d2_arr = d2_arr.copy()
print(copy_d2_arr)  
copy_d3_arr = np.copy(d3_arr) 
print(copy_d3_arr)  

# view of array

print(d1_arr.view())
print(d2_arr.view())
print(d3_arr.view())

# reshaping array

print(d1_arr)

print(d1_arr.reshape(3, 2)) # 1D to 2D
print(d1_arr.reshape(1 , 3, 2))       # 1D to 3D

print(d1_arr.reshape(3, -1)) # reshaping array into unknown dimension
print(d1_arr.reshape(3, 2, -1))

print(d2_arr.reshape(-1)) # reshaping array into 1D 
print(d3_arr.reshape(-1))

# iterating 

print("nditer")
for x in np.nditer(d2_arr): # iterating with nditer 
    print(x)

for x, y in np.ndenumerate(d2_arr): # iterating sequentially using enumeration
    print(x, y)

# join array

print("concatenate")
j1_arr = np.array([[1,3],[5,6]])
j2_arr = np.array([[22,31], [4, 2]])
join_arr = np.concatenate((j1_arr, j2_arr), axis=1) # using concatenation 
print(join_arr)

# stacking 

print("stack")
stack_arr = np.stack((j1_arr, j2_arr), axis= 1)
print(stack_arr)

print("hstack")
hs_arr = np.hstack((j1_arr, j2_arr))
print(hs_arr)

print("vstack")
vs_arr = np.vstack((j1_arr, j2_arr))
print(vs_arr)

# spliting arrray

print("split")
split_arr = np.array_split(d1_arr, 4) # axis argument can be taken
print(split_arr)

print("hsplit")
h_arr = np.hsplit(d1_arr, 3)
print(h_arr)


# search 

print("search")
print(np.where(d1_arr == 4))

# search sorted finding index to insert a particular value in array

print("searchsorted")

print(np.searchsorted(d1_arr, 8))
print(np.searchsorted(d1_arr, 8, side='right')) # passing right value to side
print(np.searchsorted(d1_arr, 8, side='left'))  # passing left value to side

# sort array in an order

print("sort")
print(np.sort(d2_arr))

# filtering array

print("filter")

f_arr = d1_arr
print(f_arr)
x = [True, False, True, False, False, False]
new_arr = f_arr[x]
print(new_arr)

y = f_arr > 4
new2_arr = f_arr[y]
print(new2_arr)
