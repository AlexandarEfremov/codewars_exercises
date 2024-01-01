word = "dennis"

for letter in word:
    keyboard = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
    find_letter = keyboard.find(letter)
    print(find_letter)
    letter_index =  divmod(keyboard.find(letter),8)
    print(letter_index)


