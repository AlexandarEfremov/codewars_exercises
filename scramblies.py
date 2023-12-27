def scramble(s1, s2):
    count_s1 = {}
    count_s2 = {}
    for char in s1:
        count_s1[char] = count_s1.get(char, 0) + 1
    for char in s2:
        count_s2[char] = count_s2.get(char, 0) + 1

    for char, count in count_s2.items():
        if count_s1.get(char, 0) < count:
            return False

    return True

print(scramble('swefzsluzv', 'wvzeflzsw'))

# https://www.codewars.com/kata/55c04b4cc56a697bb0000048