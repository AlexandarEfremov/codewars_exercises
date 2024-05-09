def secondary_check(current_number):
    same_number_index_list = []
    current_number = str(current_number)
    comparison_digi = int(current_number[0])
    smallest_so_far = None

    for index, same_digi in enumerate(current_number):
        if int(same_digi) == comparison_digi:
            same_number_index_list.append(index)

    temp_number = [n for n in str(current_number)]

    for num_in_list in same_number_index_list:
        n = temp_number.pop(num_in_list)
        temp_number.insert(0, n)
        temp_number = int("".join(temp_number))
        if temp_number < int(current_number):
            smallest_so_far = temp_number
        continue

    if smallest_so_far:
        return smallest_so_far
    return current_number


def smallest(n):
    smallest_digi = 9
    smallest_digi_index = None

    current_number = [n for n in str(n)]
    for index, num in enumerate(current_number):
        if int(num) < smallest_digi:
            smallest_digi = int(num)
            smallest_digi_index = index
    current_number.pop(smallest_digi_index)
    current_number.insert(0, str(smallest_digi))
    current_number = int("".join(current_number))

    final = secondary_check(current_number)

    return final


print(smallest(62524))