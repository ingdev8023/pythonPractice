""" ISBN-10 Validator
Given a string, determine if it's a valid ISBN-10.

An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the hyphens ("-"):

The first 9 characters must be digits, and
The final character may be a digit or the letter "X", which represents the number 10.
To validate it:

Multiply each digit (or value) by its position (multiply the first digit by 1, the second by 2, and so on).
Add all the results together.
If the total is divisible by 11, it's valid. """

import re

def is_valid_isbn10(s):
    validation = r'(\d+)-(\d+)-(\d+)-([\dX])'
     
    if re.match(validation, s):
        no_hyphens = s.replace("-","")        
        
        counter = 0
        for i in range(len(no_hyphens)):
            if no_hyphens[i] == "X":
                counter += 10 * (i + 1)
            else:
                counter += (i + 1) * int(no_hyphens[i])          
        
    else:
        return False
    
    return counter % 11 == 0


print(is_valid_isbn10("0-306-40615-2"))
print(is_valid_isbn10("0-306-40615-1"))
print(is_valid_isbn10("X-306-40615-2"))
print(is_valid_isbn10("0-8044-2957-X"))
print(is_valid_isbn10("0-6822-2589-4"))
print(is_valid_isbn10("|306-40615-X"))

#chat's
""" def is_valid_isbn10(s):
    no_hyphens = s.replace("-", "")

    if len(no_hyphens) != 10:
        return False

    if not no_hyphens[:9].isdigit():
        return False

    if not (no_hyphens[9].isdigit() or no_hyphens[9] == "X"):
        return False

    total = 0
    for i in range(10):
        value = 10 if no_hyphens[i] == "X" else int(no_hyphens[i])
        total += (i + 1) * value

    return total % 11 == 0 """