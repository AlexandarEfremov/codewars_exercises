def alphabet_war(fight):
    conversion_dict = {'j': {'w': 'm', 'p': 'q', 'b': 'd', 's': 'z'}, 't': {'m': 'w', 'q': 'p', 'd': 'b', 'z': 's'}}

    def return_opposite(char, position):
        try:
            two_positions_forward = string_as_list[position + 2]
            if two_positions_forward != "t":
                if string_as_list[index + 1]:
                    new_char = opposites[string_as_list[position + 1]]
        except IndexError:
            pass

    for index, letter in enumerate(string_as_list):



    return "Let's fight again!"



print(alphabet_war("z"))