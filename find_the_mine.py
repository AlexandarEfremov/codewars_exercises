def mine_location(field):
    minefield_as_str = "".join(map(str,[digi for arr in field for digi in arr]))
    result = divmod(minefield_as_str.find("1"), len(field))

    return list(result)

print(mine_location([  [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]  ]))

# https://www.codewars.com/kata/528d9adf0e03778b9e00067e