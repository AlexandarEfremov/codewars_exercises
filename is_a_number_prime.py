def is_prime(num):
    prime_check = True

    if num < 2:
        prime_check = False
    elif num == 2:
        prime_check = True
    elif num % 2 == 0:
        prime_check = False
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                prime_check = False
                break

    return prime_check


print(is_prime(437396593))

# https://www.codewars.com/kata/5262119038c0985a5b00029f