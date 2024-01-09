import random
f = open('words.txt', 'r')
words_text = f.read()
f.close()
words = words_text.split(' ')
answer = random.choice(words).lower()
# Imports list of 5 letter words, reads it, and selects a random word to be the answer

print('Python Wordle by Caleb Hite\nYou get 6 attempts to guess a specific 5 letter word.\nCorrect letter in the correct space: [a]\nCorrect letter in the wrong space: |a|\n')
guesses = []
counter = 6
while counter > 0:
    guess = ''
    # guess variable is used to print out the formatted guess
    new_guess = input(str(counter)+' Attempts Left, What is Your Guess?\n')
    # new_guess variable is used to compare against the answer
    if len(new_guess) != 5:
        print('Guess must have 5 letters, try again!')
    # ensures the guess is the correct length
    elif new_guess == answer:
        for l in new_guess:
            guess += '[' + l + ']'
        break
    # runs if the guess is correct
    else:
        for i in range(5):
            if new_guess[i] == answer[i]:
                guess += '[' + new_guess[i] + ']'
            elif new_guess[i] in answer:
                guess += '|' + new_guess[i] + '|'
            else:
                guess += new_guess[i]
        counter -= 1
        # runs if the guess is incorrect but valid
    guesses.append(guess)
    print('\n')
    for g in guesses:
        print(g)
else:
    print('The correct answer is '+answer)
# runs if the correct guess is never entered
    
print("Game is Over!")