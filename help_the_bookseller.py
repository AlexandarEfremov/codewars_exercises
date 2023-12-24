def stock_list(list_of_cat, list_of_art):
    sum_dict = {}
    for item in list_of_cat:
        item = item.split()
        code, value = item[0], int(item[1])
        for letter in list_of_art:
            if letter == code[0]:
                sum_dict[letter] = sum_dict.get(letter, 0)
                sum_dict[letter] += value
            else:
                sum_dict[letter] = sum_dict.get(letter, 0)
    result = [f"({key} : {value})" for key, value in sum_dict.items()]
    joined_result = " - ".join(result)
    return joined_result


b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D"]

print(stock_list(b, c))

# https://www.codewars.com/kata/54dc6f5a224c26032800005c