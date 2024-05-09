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

    return current_number


print(smallest(62524))