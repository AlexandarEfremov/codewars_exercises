def find_outlier(integers):
    evens = []
    odds = []

    for number in integers:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)

    if len(evens) > 1:
        return odds[0]
    else:
        return evens[0]


arr = [2, 4, 0, 100, 4, 11, 2602, 36]
print(find_outlier(arr))

# https://www.codewars.com/kata/5526fc09a1bbd946250002dc