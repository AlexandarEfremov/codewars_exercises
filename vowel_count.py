def get_count(sentence):
    total_vowels = 0
    for letter in sentence:
        if letter.lower() in  ("a", "e", "i", "o", "u"):
            total_vowels += 1

    return total_vowels

print(get_count("Should count all vowels"))

# https://www.codewars.com/kata/54ff3102c1bad923760001f3