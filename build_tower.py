def tower_builder(n_floors):
    floor = "*"
    space = " "
    pyramid_list = []
    for i in range (1, n_floors + 1):
        recurring_floor = ((n_floors - i) * space) + floor + ((n_floors - i) * space)
        floor += "**"
        pyramid_list.append(recurring_floor)
    return pyramid_list

print(tower_builder(3))

# https://www.codewars.com/kata/576757b1df89ecf5bd00073b