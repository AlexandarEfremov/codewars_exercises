def duplicate_encode(word):
    word = word.lower()
    unique_letters = [x for x in word if word.count(x) == 1]
    new_word = ""
    for letter in word:
        if letter in unique_letters:
            new_word += "("
        else:
            new_word += ")"
    return new_word

print(duplicate_encode("drMfTKFO"))

# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c