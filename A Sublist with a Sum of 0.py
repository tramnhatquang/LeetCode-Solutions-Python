def find_sub_zero(my_list):
    # Use hash table to store the cumulative sum as a key and
    # the element as the value till which the sum has been calculated
    # Traverse the list and return true if either
    # elem == 0 or sum == 0 or hash table already contains the sum
    # If you completely traverse the list and haven't found any
    # of the above three conditions, then simply return false
    ht = dict()
    total_sum = 0
    # Traverse through the given list
    for elem in my_list:
        total_sum += elem
        if elem == 0 or total_sum == 0 or total_sum in ht:
            return True
        ht[total_sum] = elem
    return False


my_list = [6, 4, -7, 3, 12, 9]

print(find_sub_zero(my_list)) # True
