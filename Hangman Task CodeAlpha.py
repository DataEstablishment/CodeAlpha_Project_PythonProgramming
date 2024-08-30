import random

#Cat Names
word_list = ['leopard', 'cheetah', 'tiger', 'cat', 'lion', 'panther', 'jaguar', 'cougar']

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ['_'] * word_length  # Creating a list to display blanks
lives = 7  # Number of attempts allowed

print("Welcome to Cat Hangman!")
print('You have 7 lives. Guess the word before you run out of lives!')

while lives > 0:
    print(' '.join(display))
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Correct guess!")
    else:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")

    if '_' not in display:
        print("Congratulations! You guessed the word:", chosen_word)
        break
else:
    print("Sorry, you've run out of lives. The word was:", chosen_word)
