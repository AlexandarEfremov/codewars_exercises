from itertools import groupby

def longest_repetition(chars):
    if chars == "":
        return ("", 0)
    separate_words = ["".join(group) for key, group in groupby(chars)]
    sorted_words = sorted(separate_words, key=lambda x: (-len(x), separate_words.index(x)))
    for item in sorted_words:
        item_value = item[0]
        item_len = len(item)
        item_parameters = (item_value, item_len)
        return item_parameters

print(longest_repetition(""))

# https://www.codewars.com/kata/586d6cefbcc21eed7a001155