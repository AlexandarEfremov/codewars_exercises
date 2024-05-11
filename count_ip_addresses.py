def ips_between(start, end):
    first_sum_split = start.split(".")
    second_sum_split = end.split(".")

    first_sum = (256 * (int(first_sum_split[0], int(first_sum_split[1], int(first_sum_split[2])))) +
                 int(first_sum_split[3]))
    second_sum = (256 * (int(second_sum_split[0], int(second_sum_split[1], int(second_sum_split[2])))) +
                  int(second_sum_split[3]))

    amount_of_add = second_sum - first_sum
    return amount_of_add


print(ips_between("20.0.0.10", "20.0.1.0"))
