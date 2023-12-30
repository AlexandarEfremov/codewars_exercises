def find_added(st1, st2):
    working_one = st1
    working_two = st2

    for digi in working_two:
        if digi in working_one:
            working_one = working_one.replace(digi, "", 1)
            working_two = working_two.replace(digi, "", 1)

    working_two = "".join(sorted(working_two))
    return working_two

print(find_added('4455446', '447555446666'))

# https://www.codewars.com/kata/58de77a2c19f096a5a00013f