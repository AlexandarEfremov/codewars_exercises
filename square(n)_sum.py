def square_sum(numbers):
    squared_numbers = [digi ** 2 for digi in numbers]
    sum_squared = sum(squared_numbers)
    return sum_squared


print(square_sum([1, 2, 2]))
# https://www.codewars.com/kata/515e271a311df0350d00000f