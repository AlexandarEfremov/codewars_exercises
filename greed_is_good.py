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
    dice_str = ''.join(sorted(map(str, dice)))

    for digi in dice_str:
        if digi != "2" or digi != "3" or digi != "4" or digi != "6":
            for key, value in score_key.items():
                if digi == key:
                    total_amount += value
                    digi.remove(key)


    return total_amount


print(score([5, 1, 3, 4, 1]))