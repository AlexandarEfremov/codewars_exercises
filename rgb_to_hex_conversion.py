def rgb(r, g, b):
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))

    if 0 <= r <= 15:
        r_hex = f"0{r:X}"
    else:
        r_hex = f"{r:X}"
    if 0 <= g <= 15:
        g_hex = f"0{g:X}"
    else:
        g_hex = f"{g:X}"
    if 0 <= b <= 15:
        b_hex = f"0{b:X}"
    else:
        b_hex = f"{b:X}"

    total_result = f"{r_hex}{g_hex}{b_hex}"
    return total_result

print(rgb(-115, 10, 134))

# https://www.codewars.com/kata/513e08acc600c94f01000001