""" Truncate the Text 2
Given a string, return a new string that is truncated so that the total width of the characters does not exceed 50 units.

Each character has a specific width:

Letters	Width
"ilI"	1
"fjrt"	2
"abcdeghkmnopqrstuvwxyzJL"	3
"ABCDEFGHKMNOPQRSTUVWXYZ"	4
The table above includes all upper and lower case letters. Additionally:

Spaces (" ") have a width of 2

Periods (".") have a width of 1

If the given string is 50 units or less, return the string as-is, otherwise

Truncate the string and add three periods at the end ("...") so it's total width, including the three periods, is as close as possible to 60 units without going over. """

def truncate_text(s):

    one_width = "ilI."
    two_width = 'fjrt '
    three_width = "abcdeghkmnopqrstuvwxyzJL"
    four_width = "ABCDEFGHKMNOPQRSTUVWXYZ"

    
    counter = 0

    for i in range(len(s)):      

        if s[i] in one_width:
            counter += 1
        elif s[i] in two_width:
             counter += 2
        elif s[i] in three_width:
            counter += 3
        else:
            counter += 4
        
        if counter >= 50:
            print(counter)
            return s[:i - 1] + '...'

        
    return s

print(truncate_text("The quick brown fox"))
print(truncate_text("The silky smooth sloth"))
print(truncate_text("THE LOUD BRIGHT BIRD"))
print(truncate_text("THE LOUD BRIGHT BIRD"))
print(truncate_text("The fast striped zebra"))
print(truncate_text("The big black bear"))

#chat's

def truncate_text(s):
    one_width = "ilI."
    two_width = "fjrt "
    three_width = "abcdeghkmnopqrstuvwxyzJL"
    four_width = "ABCDEFGHKMNOPQRSTUVWXYZ"

    def char_width(ch):
        if ch in one_width:
            return 1
        elif ch in two_width:
            return 2
        elif ch in three_width:
            return 3
        elif ch in four_width:
            return 4
        else:
            raise ValueError(f"Unsupported character: {ch}")

    total_width = 0
    for ch in s:
        total_width += char_width(ch)

    if total_width <= 50:
        return s

    result = ""
    current_width = 0
    ellipsis_width = 3

    for ch in s:
        w = char_width(ch)
        if current_width + w + ellipsis_width > 50:
            break
        result += ch
        current_width += w

    return result + "..."