"""Digit Rotation Escape Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count. A rotation means to move the first digit to the end. For example, after 1 rotation, 123 becomes 231. Check rotation 0 (the given number) first. Given numbers won't contain any zeros. Return the first rotation number if one is found, or "none" if not. """


def get_rotation(n): 
    counter = 0 
    rotated_n = str(n) 
    divisor = len(rotated_n) 
    
    while counter < divisor: 
        if int(rotated_n) % divisor == 0: 
            return counter 
        rotated_n = rotated_n[1:] + rotated_n[:1] 
        counter += 1 
    return 'none' 

print(get_rotation(123)) 
print(get_rotation(13579)) 
print(get_rotation(24681)) 
print(get_rotation(84138789345))