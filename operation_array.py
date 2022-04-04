import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr2 = np.array([13, 12, 11, 10, 9, 8])

#  access elemnt by index 
print('---------------------------------------')
print("print element of array :")
print(arr[5])

#  slice an array 
print('---------------------------------------')
print("Slice of an array :")
print(arr[1:5])
print(arr[1:5:2])

# data type of array 
print('---------------------------------------')
print("Data type of an array :")
print(arr.dtype)

#  create a copy of an array 
x = arr.copy()  # create a copy of an variable

# create a view of an array 
y = arr.view()  # create a reference of an variable

#  merge two array in one 
print('---------------------------------------')
temp = np.concatenate((arr, arr2))
print("Printing merge array :")
print(temp)

# split an array 
print('---------------------------------------')
print("Split an array into parts :")
newarr = np.array_split(arr2, 3)
print(newarr)

# Sort an array
print('---------------------------------------')
print("Sorted array :")
print(np.sort(arr2))
