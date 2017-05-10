def find_max_min(list_items):
    # initialize empty array to store max and min values
    max_n_min = []

    min_num = min(list_items)  # gets the maximum value in the list
    max_num = max(list_items)  # gets the minimum value in the list

    if min_num == max_num:
        max_n_min.append(len(list_items))   # gets length of the list if max and mons are equal
        return max_n_min

    max_n_min.append(min_num)
    max_n_min.append(max_num)

    return max_n_min

