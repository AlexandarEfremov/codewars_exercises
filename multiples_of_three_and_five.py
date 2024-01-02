def solution(number):
    total_sum = 0
    current_number = number - 1
    if number < 0:
        return 0
    if number == 0:
        return 0
    while current_number > 0:
        if current_number % 3 == 0 and current_number % 5 == 0:
            total_sum += current_number
            current_number -= 1
            continue
        if current_number % 3 == 0:
            total_sum += current_number
            current_number -= 1
        elif current_number % 5 == 0:
            total_sum += current_number
            current_number -= 1
        else:
            current_number -= 1
    return total_sum

print(solution(200))

# https://www.codewars.com/kata/514b92a657cdc65150000006