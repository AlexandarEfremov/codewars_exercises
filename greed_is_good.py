def score(dice):
    score_key = {
        "111": 1000,
        "666": 600,
        "555": 500,
        "444": 400,
        "333": 300,
        "222": 200,
    }

    single_score_dict = {
        "1": 100,
        "5": 50,
    }

    total_amount = 0
    dice_list = sorted(map(str, dice))
    dice_str = "".join(dice_list)

    triplet = None
    second_part = None

    for key, value in score_key.items():
        if key in dice_str:
            triplet = key
            total_amount += value
            for i in range(3):
                dice_list.remove(triplet[0])
            break

    for key, value in single_score_dict.items():
        for el in dice_list:
            if key == el:
                total_amount += value

    return total_amount


print(score([2, 4, 4, 5, 4]))

# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python