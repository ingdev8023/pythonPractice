""" For this exercise
 Write a function (guessing_game) that takes no arguments. 
 When run, the function chooses a random integer between 0 and 100
(inclusive).
 Then ask the user to guess what number has been chosen
Each time the user enters a guess, the program indicates one of the following:
– Too high
– Too low
– Just right
 If the user guesses correctly, the program exits. Otherwise, the user is asked to
try again.
 The program only exits after the user guesses correctly
 """
import random
def guessing_game():
    random_number = random.randint(0,20)
    counter = 2
    while counter >= 0:
        number = int(input('Enter a number between 0 and 20: '))           
              
        if number > random_number:
            print(f"Too High, chances remaining: {counter}")
            counter -= 1
        elif number  < random_number:
            print(f"Too Low, chances remaining: {counter}")
            counter -= 1
        else:
            return print('just right')  
    print(f'No more chances remaining')
guessing_game()    