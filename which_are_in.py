def in_array(arr_one, arr_two):
    array_list = []
    for array in arr_one:
        for element in arr_two:
            if array in element:
                array_list.append(array)
                break
    unique_list = list(set(array_list))
    unique_list.sort()
    return unique_list


array_one = ["live", "arp", "strong"]
array_two = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(array_one, array_two))