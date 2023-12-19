def solution(number):
    temp_sum = 0
    current_number = number - 1
    if number < 0:
        temp_sum = 0
    else:
        while current_number > 0:
            if current_number % 3 == 0 and current_number % 5 == 0:
                temp_sum += current_number
                current_number -= 1
                continue
            if current_number % 3 == 0:
                temp_sum += current_number
            elif current_number % 5 == 0:
                temp_sum += current_number
            current_number -= 1

    return temp_sum

print(solution(16))

# https://www.codewars.com/kata/514b92a657cdc65150000006