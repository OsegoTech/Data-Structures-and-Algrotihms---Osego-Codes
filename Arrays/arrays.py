array = [1,2,3,4,5,6]
print(array)

# append or insert an element to the array - on avarage O(1) time complexity
array.append(7)
print(array)

# insert an element at a specific index - O(n) time complexity
array.insert(0, 0)
print(array)

# remove an element from the array - O(n) time complexity
array.remove(0)
print(array)

# remove the last element from the array - O(1) time complexity
array.pop()
print(array)

# remove an element at a specific index - O(n) time complexity
array.pop(0)
print(array)

# find the index of an element in the array - O(n) time complexity
print(array.index(4))

# check if an element is in the array - O(n) time complexity
print(4 in array)

# sort the array - O(nlogn) time complexity
array.sort()
print(array)

# reverse the array - O(n) time complexity
array.reverse()
print(array)

# copy the array - O(n) time complexity
array_copy = array.copy()
print(array_copy)

# clear the array - O(n) time complexity
array.clear()
print(array)

# create an array with a specific size and default value
array = [0] * 5
print(array)

# create an array with a specific size and default value
array = [0 for _ in range(5)]
print(array)

# create an array with a specific size and default value
array = [i for i in range(5)]
print(array)

# create an array with a specific size and default value

array = [i for i in range(5) if i % 2 == 0]
print(array)

# create a 2D array
array = [[0] * 5 for _ in range(5)]
print(array)

# create a 2D array
array = [[0 for _ in range(5)] for _ in range(5)]
print(array)

# create a 2D array

array = [[i for i in range(5)] for _ in range(5)]
print(array)
