def find_maximum(lst):
    # check if list is empty
    if not lst:
        return None
      
    # Initialize the maximum value to the first element in the list
    max_value = lst[0]

    # iterate through the list
    for num in lst:
        if num > max_value:
            max_value = num

    return max_value