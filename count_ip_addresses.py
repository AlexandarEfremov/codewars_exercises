def ips_between(start, end):
    amount_of_add = 0
    first_sum_split = start.split(".")
    second_sum_split = start.split(".")
    return first_sum_split, second_sum_split


print(ips_between("10.0.0.0", "10.0.0.50"))
