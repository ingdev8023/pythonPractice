

# Exercise 1 — Squares
test =  [1,2,3,4]

def squares(numbers):
    return [x*x for x in numbers]

print(squares(test))

# Exercise 2 — Count vowels


def countingVocals(word):
    vowels = ['a','e','i','o','u']
    total_vowels = [x for x in word if x in vowels]
    return len(total_vowels) 
test_word_1 = 'programming'
print(countingVocals(test_word_1))

# Exercise 3 — Reverse word

def reversed_word(word):
    list_word = list(word)
    list_word.reverse()
    return ''.join(list_word)

test_word_2 = 'hello'
print(reversed_word(test_word_2))



# Exercise 4 — Max number

def max_number(numbers):

    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n

    return max_value

test_numbers = [4,7,1,9,3]
print(max_number(test_numbers))

# Exercise 5 — Remove duplicates

def no_duplicates(numbers):
    clean_list= []
    for x in numbers:
        if x not in clean_list:
            clean_list.append(x)
    return clean_list

test_number_2  = [1,2,2,3,4,4,5]   
print(no_duplicates(test_number_2))

# Exercise 6 — Student with highest grade

test_dict_students = {
"Luis":75,
"Carlos":60,
"Ana":90,
}

def max_note(notes):
    name = ""
    note = 0
    for y, x in notes.items():
        if x > note:
            note = x
            name = y
    return name
print(max_note(test_dict_students))

# Exercise 7 — Count letters

def counting_letters(word):
    letters_dict = {}
    for x in word:
        if x in letters_dict:
           letters_dict[x] += 1
        else: 
            letters_dict[x] = 1 
    return letters_dict

test_word_3 = 'banana'
print(counting_letters(test_word_3))

# Exercise 8 — Palindrome

def palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word

print(palindrome('python'))

# Exercise 9 — Even numbers

def even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]

test_number_3 =[1,2,3,4,5,6]
print(even_numbers(test_number_3))