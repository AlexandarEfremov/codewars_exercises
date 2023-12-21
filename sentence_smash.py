def smash(words):
    sentence = ''
    for word in words:
        if word == words[-1]:
            word = word.strip()
            sentence += word
        else:
            word = word.strip()
            sentence += word + " "
    return sentence


print(smash(['hello', 'world', 'this', 'is', 'great']))

# https://www.codewars.com/kata/53dc23c68a0c93699800041d