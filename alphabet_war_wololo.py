def alphabet_war(fight):
    string_as_list = [x for x in fight]

    left = {
        "w": 4,
        "p": 3,
        "b": 2,
        "s": 1,
        "t": 0,
    }

    right = {
        "m": 4,
        "q": 3,
        "d": 2,
        "z": 1,
        "j": 0,
    }

    opposites = {
        "w": "m",
        "p": "q",
        "b": "d",
        "s": "z",
        "z": "s",
        "d": "b",
        "q": "p",
        "m": "w",
    }
    for letter in string_as_list:
        if letter == "j" or letter == "t":


    return "Let's fight again!"



print(alphabet_war("z"))