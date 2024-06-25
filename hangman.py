from ascii import stages, logo
from random_word import RandomWords
import os

# TODO-1 - Randomly choose a word and assign it to a variable called chosen_word.
r = RandomWords()
chosen_word = r.get_random_word()
print(chosen_word)
# TODO-3: - Create an empty List called display.
display = []
# TODO-7: - Create a variable called 'lives' to keep track of the number of lives left.
lives = 6

for _ in enumerate(chosen_word):
    # For each letter in the chosen_word, add a "_" to 'display'.
    # So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
    display.append('_')

# TODO-10: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

# TODO-6: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
playing = True
while playing:
    # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter\n").lower()
    # TODO-11: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f'You already picked letter {guess}. Choose another letter')
    if guess not in chosen_word:
        # TODO-8: - If guess is not a letter in the chosen_word,
        # Then reduce 'lives' by 1.
        # If lives goes down to 0 then the game should stop and it should print "You lose."
        lives -= 1
        # TODO-12: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
        if lives == 0:
            playing = False
            print(f'You lose \n the chosen word was: {chosen_word}')
    # TODO-4: - Loop through each position in the chosen_word;
    for index, letter in enumerate(chosen_word):
        # print(letter, 'letter')
        # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        if letter == guess:
            # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
            # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
            display[index] = guess

        if ''.join(display) == chosen_word:
            playing = False
            print('You win')
    # TODO-9: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
    print(f"Number of lives:{lives}")
    # TODO-5: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    print(''.join(display))

# print(f'Pssst, the solution is {chosen_word}')

