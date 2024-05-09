def smallest(n):
    number_as_str_list = [n for n in str(n)]
    num_copy = number_as_str_list.copy()

    smallest_single_digi = min([int(n) for n in number_as_str_list])

    temp_smallest = n
    temp_smallest_digi_index = None

    for index, digi in enumerate(number_as_str_list):
        if int(digi) == smallest_single_digi:
            extract = num_copy.pop(index)
            num_copy.insert(0, extract)
            new_value_as_int = int("".join(num_copy))
            if new_value_as_int < n:
                temp_smallest = new_value_as_int
                temp_smallest_digi_index = index
            num_copy = number_as_str_list

    return temp_smallest, temp_smallest_digi_index, 0


print(smallest(209917))
