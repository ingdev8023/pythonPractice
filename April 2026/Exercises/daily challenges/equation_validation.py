"""Equation Validation
Given a string representing a math equation, determine whether it is correct.

The left side may contain up to three positive integers and the operators +, -, *, and /.
The equation will be given in the format: "number operator number = number" (with two or three numbers on the left). For example: "2 + 2 = 4" or "2 + 3 - 1 = 4".
The right side will always be a single integer.
Follow standard order of operations: multiplication and division are evaluated before addition and subtraction, from left-to-right."""

import re
import operator

def is_valid_equation(equation):
    operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    }
    priority = {"*", "/"}
    pattern = r"(\d+)\s([-*+/])\s(\d+)\s(([+-/*])\s(\d+)\s)?=\s(\d+)"
    equation_match = re.fullmatch(pattern, equation)


    if not equation_match:
        return False

    first_number = int(equation_match.group(1))
    second_number = int(equation_match.group(3))
    first_operator = equation_match.group(2)
    result = int(equation_match.group(7))

    if not equation_match.group(4):
        return result == operations[first_operator](first_number, second_number)   

    third_number =  int(equation_match.group(6))
    second_operator= equation_match.group(5)
    final_value = 0
    
    if first_operator in priority and second_operator not in priority:
        temp = operations[first_operator](first_number, second_number)
        final_value = operations[second_operator](third_number, temp)      

    elif  second_operator in priority and first_operator not in priority:         
        temp = operations[second_operator](second_number,third_number)
        final_value = operations[first_operator](first_number, temp)
    else:    
        temp = operations[first_operator](first_number, second_number)
        final_value = operations[second_operator](third_number, temp)      
    
    
    return result == final_value 

print(is_valid_equation("2 + 2 = 4") )
print(is_valid_equation("2 + 3 - 1 = 4"))
print(is_valid_equation("20 - 2 * 3 = 14"))
print(is_valid_equation("8 / 2 = 4"))
print(is_valid_equation("2 + 5 = 6"))
print(is_valid_equation("10 - 2 * 3 = 24"))
print(is_valid_equation("10000 + 10000 = 20000"))
print(is_valid_equation("40000 + 10000 = 20000"))
print(is_valid_equation("8 / 2 * 2 = 8"))
print(is_valid_equation("8 / 2 / 4 = 1"))