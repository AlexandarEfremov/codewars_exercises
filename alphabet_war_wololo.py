def alphabet_war(fight):
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

    def conversion(wolo, position, string):
        one_pos_forward = string[position + 1]
        two_pos_forward = string[position + 2]
        one_pos_backwards = string[position - 1]
        two_pos_backwards = string[position - 2]

        if wolo == "t":
            if wolo[position - 1]:
                if wolo[position - 2]:
                    if wo

    wololos = [{wolo: index} for index, wolo in enumerate(fight) if wolo in "tj"]
    if wololos:
        for i in wololos:
            for wolo, pos in i.items():

    return "Let's fight again!"



print(alphabet_war("z"))