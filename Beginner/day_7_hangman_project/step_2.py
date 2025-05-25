import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

# Create a "placeholder" with the same number of blanks as the chosen_word.
placeholder = ""
word_length = len(chosen_word)
for num in range(word_length):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

# Create a "display" that puts the guess letter in the right position.
display = ""

for letter in chosen_word:
    if guess == letter:
        display += letter
    else:
        display += "_"

print(display)
