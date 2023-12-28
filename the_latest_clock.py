from itertools import permutations
def late_clock(a, b, c, d):
    numbers = [str(a), str(b), str(c), str(d)]

    all_permutations = permutations(numbers, 4)
    maximum_time = "00:00"

    for perm in all_permutations:
        hour = perm[0] + perm[1]
        minute = perm[2] + perm[3]

        time_string = hour + ":" + minute
        if "00" <= hour <= "23" and "00" <= minute <= "59":
            if time_string > maximum_time:
                maximum_time = time_string
    return maximum_time


print(late_clock(0, 0, 4, 2))

# https://www.codewars.com/kata/58925dcb71f43f30cd00005f