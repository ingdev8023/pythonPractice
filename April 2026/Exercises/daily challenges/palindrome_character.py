"""Palindrome Characters
Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

A palindrome is a string that is the same forward and backward.
If it's not a palindrome, return "none"."""

def palindrome_locator(s):
    new_word = s[::-1]

    if s == new_word:
        if len(s) % 2 != 0:
           return s[int((len(s) - 1)/2)]
        else:
            return s[int(len(s)/2) -1] + s[(int(len(s)/2))]
    
    return 'none'
print(palindrome_locator("racecar"))
print(palindrome_locator("noon"))
print(palindrome_locator("level"))
print(palindrome_locator("freecodecamp"))
print(palindrome_locator("11100111"))