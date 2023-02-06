def find_symmetric(my_list):
    # Write your code here
    hash_table = {}
    res = []
    for sublist in my_list:
        key, val = sublist[0], sublist[1]
        if val in hash_table: # check if symmertric pair exists
            if hash_table[val] == key:  
                res.append(sublist)
                res.append([val, key])
        else:
            hash_table[key] = val
    return res
    # time: O(n), n is length of list

arr = [[1, 2], [4, 6], [4, 3], [6, 4], [5, 9], [3, 4], [9, 5]]
symmetric = find_symmetric(arr)
print(symmetric)






