def beggars(values, n):
    donations = values
    beggar_dict = {}
    total_donations = []
    if n == 0:
        return total_donations

    while True:
        break_cond = False
        for beggar in range(1, n + 1):
            beggar_dict[beggar] = beggar_dict.get(beggar, 0)

        for beggar in range(1, n + 1):
            if len(donations) == 0:
                break_cond = True
                break
            else:
                beggar_dict[beggar] += donations[0]
                donations.pop(0)
        if break_cond:
            break
    for value in beggar_dict.values():
        total_donations.append(value)
    return total_donations
print(beggars([1,2,3,4,5],6))

# https://www.codewars.com/kata/59590976838112bfea0000fa