""" Longest Consecutive Character

Given a string, return the character that appears in the longest consecutive streak and the length of that streak. """

def longest_consecutive(word):
    if not word:
        return None

    max_char = word[0]
    max_count = 1

    current_char = word[0]
    current_count = 1

    for i in range(1, len(word)):
        if word[i] == current_char:
            current_count += 1
        else:
            current_char = word[i]
            current_count = 1

        if current_count > max_count:
            max_char = current_char
            max_count = current_count

    return (max_char, max_count)

print(longest_consecutive("aaabbccccd"))
print(longest_consecutive("hello"))
print(longest_consecutive("zzzzzz"))
print(longest_consecutive("abc"))