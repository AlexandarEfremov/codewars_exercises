def friend(x):
    friend_list = []
    for name in x:
        if len(name) == 4:
            friend_list.append(name)
    return friend_list

print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))

# https://www.codewars.com/kata/55b42574ff091733d900002f