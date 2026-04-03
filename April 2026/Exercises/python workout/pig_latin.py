def pig_lating(word):
    vowels = ['a','e','i','o','u']

    if word[0] in vowels:
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

print(pig_lating('computer'))
print(pig_lating('python'))