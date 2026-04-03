def hex_output():
    number= input('Insert the Hexadecimal Number:')
    reversed_number = number[::-1]
    decimal_number = 0
    for i, char in enumerate(reversed_number):
        decimal_number += int(char) * (16 ** i)
    return decimal_number

print(hex_output())