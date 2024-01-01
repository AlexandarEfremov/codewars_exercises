def longer(st):
    words = st.split()
    sorting_function = sorted(words, key=lambda x: (len(x), x))
    return " ".join(sorting_function)

print(longer("Have you ever Seen the Rain"))

# https://www.codewars.com/kata/5963314a51c68a26600000ae
# The kata has errors with the leading empty spaces in the random tests, author is trying to remove this, otherwise solved