""" First Non-Repeating Consecutive Break

Given a string, return the first character that breaks a consecutive repeat streak.

A character “breaks a streak” if:

the character immediately before it is the same as the previous one, and
the current character is different

In other words, find the first character that appears right after a repeated consecutive group.

If no such character exists, return None. """

def break_repeating(word):
    for i in range(2, len(word)):
        if word[i - 2] == word[i - 1] and word[i] != word [i - 1]:
            return word[i]
    return None

print(break_repeating("aaabbcdd"))
print(break_repeating('helloo'))
print(break_repeating("aabccdee"))
print(break_repeating("abc"))
print(break_repeating("xxxxyzz"))
print(break_repeating("abba"))
print(break_repeating("aaab"))
print(break_repeating("zzzyx"))
print(break_repeating("aa"))
