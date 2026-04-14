from collections import Counter
def most_repeating_word(words):
    words_list = words.split(" ")
    final_word= ''
    counter = 0
    for word in words_list:
        if Counter(word).most_common(1)[0][1] > 1 and Counter(word).most_common(1)[0][1] > counter:
            final_word = word
            counter = Counter(word).most_common(1)[0][1]       

    return final_word

print(most_repeating_word('this is an elementary test example'))