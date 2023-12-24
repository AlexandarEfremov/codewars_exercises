def sum_dig_pow(a, b):
    eureka_numbers = []
    for number in range(a, b + 1):
        temp_number = 0
        for index, digit in enumerate(str(number)):
            current_number = int(digit) ** (index + 1)
            temp_number += current_number
        if temp_number == number:
            eureka_numbers.append(number)
        else:
            continue

    return eureka_numbers

print(sum_dig_pow(1, 100))

# https://www.codewars.com/kata/5626b561280a42ecc50000d1