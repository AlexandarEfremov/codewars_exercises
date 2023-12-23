def good_vs_evil(good, evil):
    good_split = [int(digi) for digi in good.split()]
    bad_split = [int(digi) for digi in evil.split()]

    hobbit, men, elves, dwarves, eagles, wizards = good_split[0], (2 * good_split[1]), (3 * good_split[2]), \
        (3 * good_split[3]), (4 * good_split[4]), (10 * good_split[5])
    orcs, men_two, wargs, goblins, uruk, trolls, wizards_two = bad_split[0], (2 * bad_split[1]), (2 * bad_split[2]), \
        (2 * bad_split[3]), (3 * bad_split[4]), (5 * bad_split[5]), (10 * bad_split[6])

    sum_good = (hobbit + men + elves + dwarves + eagles + wizards)
    sum_bad = (orcs + men_two + wargs + goblins + uruk + trolls + wizards_two)

    if sum_good > sum_bad:
        return "Battle Result: Good triumphs over Evil"
    elif sum_bad > sum_good:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"


print(good_vs_evil('0 0 0 1 0 0', '0 0 0 0 1 0 0'))

# https://www.codewars.com/kata/52761ee4cffbc69732000738