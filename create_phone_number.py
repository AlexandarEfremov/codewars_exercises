def create_phone_number(n):
    parentheses_block = n[:3]
    first_triplet = n[3:6]
    last_quartet = n[6:]

    formatted_num = f"({''.join(map(str, parentheses_block))}) {''.join(map(str, first_triplet))}-{''.join(map(str, last_quartet))}"
    return formatted_num

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# "(123) 456-7890"

# https://www.codewars.com/kata/525f50e3b73515a6db000b83