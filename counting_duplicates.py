def duplicate_count(text):
    text_lower = text.lower()
    unique_chars = set()
    total_count = 0

    for letter in text_lower:
        if letter.isalnum() and letter not in unique_chars:
            temp_count = text_lower.count(letter)
            if temp_count > 1:
                total_count += 1
            unique_chars.add(letter)

    return total_count

# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1