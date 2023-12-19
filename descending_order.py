def descending_order(num):
    if num > 0:
        sorted_num = sorted(str(num), reverse=True)
        sorted_num = "".join(sorted_num)
        sorted_num = int(sorted_num)
    else:
        sorted_num = 0
    return sorted_num


print(descending_order(6532))

# https://www.codewars.com/kata/5467e4d82edf8bbf40000155