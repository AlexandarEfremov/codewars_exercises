def score(dice):
    score_key = {
        "111": 1000,
        "666": 600,
        "555": 500,
        "444": 400,
        "333": 300,
        "222": 200,
        "1": 100,
        "5": 50
    }
    total_amount = 0
    dice_str = sorted(map(str, dice))

    first_triplet = dice_str[:3]
    second_part = dice_str[3:]

    first_triplet_as_str = "".join(first_triplet)

    for key, value in score_key.items():
        if first_triplet_as_str == key:
            total_amount += value
        else:
            for el in first_triplet:
                if el == key:
                    total_amount += value

    for key, value in score_key.items():
        for el in second_part:
            if el == key:
                total_amount += value

    return second_part


print(score([5, 1, 3, 4, 1]))
