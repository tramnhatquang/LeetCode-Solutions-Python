def trace_path(my_dict):  # A Map object
    # Write your code here
    # 1. find the starting location of the whole journey/itineray
    # 2. starting from the first location, continue to find the destination.
    # 3. Update the from = destionation and continue to append all the continuous journey into the res arr
    res = []

    # find the reverse dic
    reverse_dict = {}
    for key, val in my_dict.items():
        reverse_dict[val] = key

    # find the starting loc by checking keys of one dict to another one. If a key does not belong to keys of reverse dict,
    # in otherwords, its does not have a dest. That's our starting point
    from_location = None
    for key in my_dict:
        if key not in reverse_dict:
            from_location = key
            break

    dest = my_dict.get(from_location)
    while dest:
        res.append([from_location, dest])
        from_location = dest
        dest = my_dict.get(dest)

    return res
    # time: O(n), n is the number of journeys


my_dict = dict()
my_dict["NewYork"] = "Chicago"
my_dict["Boston"] = "Texas"
my_dict["Missouri"] = "NewYork"
my_dict["Texas"] = "Missouri"
print(trace_path(my_dict))