def wise_speak(sentence):
    wise_words = ["have", "must", "are", "will", "can"]
    punctuation = sentence[-1]
    sentence = sentence[:-1]
    list_sentence = sentence.lower().split()
    for word in wise_words:
        for wise in list_sentence:
            if word == wise:
                after = list_sentence[list_sentence.index(word) + 1:] 
                before = list_sentence[0:list_sentence.index(word) + 1]
                new_sentence = " ".join(after).capitalize() + ', ' + ' '.join(before) + punctuation
                print(new_sentence)
                return new_sentence
            else:
                'No wise word found'

wise_speak("You must speak wisely.")
wise_speak("You can do it!")
wise_speak("Do you think you will complete this?")
wise_speak("All your base are belong to us.")
wise_speak("You have much to learn.")