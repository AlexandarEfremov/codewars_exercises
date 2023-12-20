def two_sum(numbers, target):
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers[i + 1:], start=i + 1):
            if x + y == target:
                return i, j

result = two_sum([2, 2, 3], 4)
print(result)

# https://www.codewars.com/kata/52c31f8e6605bcc646000082