def ips_between(start, end):
    first_sum_split = start.split(".")
    second_sum_split = end.split(".")

    first_sum_split = [int(x) for x in first_sum_split]
    second_sum_split = [int(x) for x in second_sum_split]

    first_sum = (256 * sum(first_sum_split[:-1])) + first_sum_split[-1]
    second_sum = (256 * sum(second_sum_split[:-1])) + second_sum_split[-1]

    return second_sum - first_sum


print(ips_between("20.0.0.10", "20.0.1.0"))
