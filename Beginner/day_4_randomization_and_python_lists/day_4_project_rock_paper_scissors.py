import random

choices = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if user_choice < 0 or user_choice >= len(choices):
    print("Invalid choice")
else:
    com_choice = random.randint(0, len(choices) - 1)
    print("You chose:")
    print(choices[user_choice])
    print("Computer chose:")
    print(choices[com_choice])

    if user_choice == com_choice:
        print("Draw")
    else:
        if user_choice == 0:
            if com_choice == 1:
                print("You lose")
            elif com_choice == 2:
                print("You win")
        elif user_choice == 1:
            if com_choice == 0:
                print("You win")
            elif com_choice == 2:
                print("You lose")
        elif user_choice == 2:
            if com_choice == 0:
                print("You lose")
            elif com_choice == 1:
                print("You win")
