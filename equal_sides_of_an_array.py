def find_even_index(arr):
    result = 0
    str_array = [str(digi) for digi in arr]
    for index, number in enumerate(str_array):
        left_sum = sum([int(digi) for digi in str_array[:index]])
        right_sum = sum([int(digi) for digi in str_array[index + 1:]])
        if left_sum == right_sum:
            result = index
            break
        else:
            result = -1
    return result


ray = [1,2,3,4,3,2,1]
print(find_even_index(ray))

# https://www.codewars.com/kata/5679aa472b8f57fb8c000047