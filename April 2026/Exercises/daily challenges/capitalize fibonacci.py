"""Capitalized Fibonacci
Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

The first character is at index 0.
If the index of non-letter characters is a Fibonacci number, leave it unchanged."""

def capitalize_fibonacci(s):
    fibo_numbers = [0,1]
    capitalize_word = ''

    for i in range(2,len(s)):  
             
        fibo_numbers.append(fibo_numbers[i - 1] + fibo_numbers[i - 2])
        
    
    for i in range(len(s)):

        if i in fibo_numbers:
            capitalize_word = capitalize_word + s[i].upper()
        else:
            capitalize_word = capitalize_word + s[i].lower()    

    return capitalize_word


print(capitalize_fibonacci("hello world"))
print(capitalize_fibonacci("HELLO WORLD"))

#chat's 

def capitalize_fibonacci(s):
    fib_indices = {0, 1}
    a, b = 0, 1

    while b < len(s):
        fib_indices.add(b)
        a, b = b, a + b

    chars = []

    for i, ch in enumerate(s):
        if i in fib_indices:
            chars.append(ch.upper())
        else:
            chars.append(ch.lower())

    return "".join(chars)