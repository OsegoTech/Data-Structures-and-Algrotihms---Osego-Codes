def find_smallest(arr):
    smallest = arr[0] # Stores the smallest value
    smallest_index = 0 # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print(find_smallest([5, 3, 6, 2, 10])) # 3

def selection_sort(arr): # Sorts an array
    new_arr = [] # Stores the sorted array
    for i in range(len(arr)): # Finds the smallest element in the array and adds it to the new array
        smallest = find_smallest(arr) # Finds the smallest element in the array
        new_arr.append(arr.pop(smallest)) # Adds the smallest element to the new array
    return new_arr

print(selection_sort([5, 3, 6, 2, 10])) # [2, 3, 5, 6, 10]