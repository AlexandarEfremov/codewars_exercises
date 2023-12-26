def disemvowel(string):
    vowels = "aeoiu"
    for letter in string:
        if letter.lower() in vowels:
            string = string.replace(letter, "")
    return string

print(disemvowel("This website is for losers LOL!"))

# https://www.codewars.com/kata/52fba66badcd10859f00097e
