import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# Check if the letter  the user guessed is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it
# is not.
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")
