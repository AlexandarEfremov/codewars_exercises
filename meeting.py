def meeting(s):
    user_list = []
    s = s.split(";")
    for personal_info in s:
        name, surname = personal_info.upper().split(":")[0], personal_info.upper().split(":")[1]
        user_list.append((surname, name))
    sorted_list = sorted(user_list)
    result_string = "".join(["({}, {})".format(surname, name) for surname, name in sorted_list])
    return result_string


print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"))

# https://www.codewars.com/kata/59df2f8f08c6cec835000012