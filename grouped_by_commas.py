def group_by_commas(n):
    n_reversed = str(n)
    result = ''
    number_counter = 0
    for index, digi in enumerate(n_reversed[::-1]):
        if number_counter % 3 == 0 and index != 0:
            result += ","
            number_counter = 0
            result += str(digi)
            number_counter += 1
        else:
            result += str(digi)
            number_counter += 1
    flipped_result = result[::-1]
    return flipped_result

print(group_by_commas(351237678954235))
# https://www.codewars.com/kata/5274e122fc75c0943d000148