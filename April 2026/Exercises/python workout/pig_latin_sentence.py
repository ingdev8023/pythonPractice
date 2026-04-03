def pl_sentence(sentence):

    vowels = ['a','e','i','o','u']
    sentence_list = sentence.split(' ')
    final_word = ''

    for i in sentence_list:
        if i[0] in vowels:
            final_word += i + 'way' + ' '
        else:
            final_word +=  i[1:] +  i[0] + 'ay' + ' '
    
    return final_word


print(pl_sentence('this is a test translation'))