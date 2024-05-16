def alphabet_war(fight):
    initial_score = 0
    alpha_dict = {
                   "w": 4,
                   "p": 3,
                   "b": 2,
                   "s": 1,
                   "m": -4,
                   "q": -3,
                   "d": -2,
                   "z": -1
                   }
    for letter in fight:
        initial_score += alpha_dict.get(letter, 0)

    return ["Right side wins!", "Left side wins!"][initial_score > 0] if initial_score else "Let's fight again!"
