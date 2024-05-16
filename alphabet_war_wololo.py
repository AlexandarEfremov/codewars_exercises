def alphabet_war(fight):
    conversion_dict = {'j': {'w': 'm', 'p': 'q', 'b': 'd', 's': 'z'}, 't': {'m': 'w', 'q': 'p', 'd': 'b', 'z': 's'}}

    initial_score = 0

    for left, center, right in zip(" " + fight, fight, fight[1:] + " "):
        if left + right not in 'tjt':
            center = conversion_dict.get(left, {}).get(center, center)
            center = conversion_dict.get(right, {}).get(center, center)
        initial_score += {'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1}.get(center, 0)

    return ["Right side wins!", "Left side wins!"][initial_score > 0] if initial_score else "Let's fight again!"


print(alphabet_war("wololooooo"))

#assisted solution
#NOTE Python treats True as 1 and False as 0 in arithmetic operations., which helps in slicing the return statement