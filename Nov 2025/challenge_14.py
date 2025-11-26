# GCD
# Given two positive integers, return their greatest common divisor (GCD).

# The GCD of two integers is the largest number that divides evenly into both numbers without leaving a remainder.
# For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6. So given 4 and 6, return 2, the largest number that appears in both sets of divisors.

def gcd(x, y):
    divisors = [n for n in range(1,x + 1) if x % n  == 0 and y % n  == 0]    
    return max(divisors)    