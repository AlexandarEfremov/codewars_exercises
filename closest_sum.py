from itertools import combinations

def closest_sum(ints, num):
    all_permutation = combinations(ints, 3)
    printouts = set([sum(x) for x in all_permutation])
    closest = min(printouts, key=lambda x: abs(num - x))
    return closest

print(closest_sum([2, -5, -9, 1, 4, 8], -1))

# https://www.codewars.com/kata/577e694af5db624cf30002d0