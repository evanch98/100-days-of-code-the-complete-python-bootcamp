print("""
**************************
         __________
        /\\____;;___\\
       | /         /
       `. ())oo() .
        |\\(%()*^^()^\\
       %| |-%-------|
      % \\ | %  ))   |
      %  \\|%________|
**************************
""")
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a cross road. Where do you want to go?")
direction = input('    Type "left" or "right" ')
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    action = input('    Type "wait" to wait for a boat. Type "swim" to swim across. ')
    if action == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door_color = input("    One red, one yellow, and one blue. Which color do you choose? ")
        if door_color == "blue":
            print("You were eaten by beasts. Game Over.")
        elif door_color == "red":
            print("You were burned by fire. Game Over.")
        elif door_color == "yellow":
            print("You found the treasure. You Win!")
        else:
            print("Game Over.")
    else:
        print("You were attacked by trout. Game Over.")
else:
    print("You fall into a hole. Game over.")
