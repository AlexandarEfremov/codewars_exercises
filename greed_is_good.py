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

    return dice_str


print(score([5, 1, 3, 4, 1]))
