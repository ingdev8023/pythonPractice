def ubbi_dubbi(word):
    vowels = ['a','e','i','o','u']
    new_word = ''

    for i in word:
        if i in vowels:
            new_word += "ub" + i
        else:
            new_word += i 
    return new_word

print(ubbi_dubbi('elephant'))