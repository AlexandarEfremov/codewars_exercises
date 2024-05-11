def ips_between(start, end):
    first_sum_split = start.split(".")
    second_sum_split = end.split(".")

    first_sum_split = [int(x) for x in first_sum_split]
    second_sum_split = [int(x) for x in second_sum_split]

    first_sum = (first_sum_split[0] * (256 ** 3)) + (first_sum_split[1] * (256 ** 2)) + (first_sum_split[2] * 256) + first_sum_split[3]
    second_sum = (second_sum_split[0] * (256 ** 3)) + (second_sum_split[1] * (256 ** 2)) + (second_sum_split[2] * 256) + second_sum_split[3]

    return second_sum - first_sum


print(ips_between("176.22.241.151", "176.23.12.7"))
