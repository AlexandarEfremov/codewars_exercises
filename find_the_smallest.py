def smallest(n):
    smallest_num = n
    string_number = str(n)
    ran = range(len(string_number))
    x = None
    y = None
    for i in ran:
        for j in ran:
            temp_list = list(string_number)
            index_var = temp_list.pop(i)
            temp_list.insert(j, index_var)
            result = int("".join(temp_list))
            if result < smallest_num:
                smallest_num = result
                x = i
                y = j
    return [smallest_num, x, y]


print(smallest(209917))

# https://www.codewars.com/kata/573992c724fc289553000e95/python