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
    str_len = len(fight)
    if str_len == 1:
        if fight in left:
            return "Left side wins!"
        elif fight in right:
            return "Right side wins!"

    return "Let's fight again!"


print(alphabet_war("z"))