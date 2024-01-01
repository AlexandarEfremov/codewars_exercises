def prime_bef_aft(num):
    bef_aft_list = []
    after_number = num + 1
    before_number = num - 1
    while True:
        lower_prime = True
        for lo in range(2, before_number):
            if before_number % lo == 0:
                lower_prime = False
                break
        if lower_prime:
            bef_aft_list.append(before_number)
            break
        else:
            before_number -= 1
    while True:
        is_prime = True
        for nu in range(2, num - 1):
            if after_number % nu == 0:
                is_prime = False
                break
        if is_prime:
            bef_aft_list.append(after_number)
            break
        else:
            after_number += 1

    return bef_aft_list

print(prime_bef_aft(101))
# https://www.codewars.com/kata/560b8d7106ede725dd0000e2
