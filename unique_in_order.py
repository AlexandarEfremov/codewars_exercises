def unique_in_order(sequence):
    unique_list = []
    for letter in sequence:
        if letter not in unique_list or letter != unique_list[-1]:
            unique_list.append(letter)
    return unique_list

print(unique_in_order('AAAABBBCCDAABBB'))

# https://www.codewars.com/kata/54e6533c92449cc251001667