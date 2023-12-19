def square_digits(num):
    squared_number = [int(digi) ** 2 for digi in str(num)]
    result = int("".join(map(str, squared_number)))
    return result


print(square_digits(9119))

# https://www.codewars.com/kata/546e2562b03326a88e000020