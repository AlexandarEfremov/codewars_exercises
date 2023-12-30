def getlocation(letter):
    keyboard = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    letter_location = divmod(keyboard.find(letter), 8)
    return letter_location


def tv_remote(word):
    x_one = 0
    y_one = 0
    total_steps = 0
    for letter in word:
        x_two, y_two = getlocation(letter)
        current_steps = abs(x_one - x_two) + abs(y_one - y_two) + 1
        total_steps += current_steps
        x_one, y_one = x_two, y_two
    return total_steps


print(tv_remote("does"))

# https://www.codewars.com/kata/5a5032f4fd56cb958e00007a