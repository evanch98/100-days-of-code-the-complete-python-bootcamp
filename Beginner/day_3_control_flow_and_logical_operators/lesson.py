# # Control Flow and Conditional Operators
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You can ride the rollercoaster.")
# else:
#   print("Sorry you have to grow taller before you can ride.")

# # Modulo Operator
# 10 % 5  # 0 (no remainder)
# 10 % 3  # 1
# num = int(input("Enter a number: "))
# result = num % 2
# if (result == 0):
#   print("It's an even number.")
# else:
#   print("It's an odd number.")

# # Nested if statements and elif statements
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You can ride the rollercoaster.")
#   age = int(input("How old are you? "))
#   if age <= 12:
#     print("Please pay $5.")
#   elif age >= 18:
#     print("Please pay $12.")
#   else:
#     print("Please pay $7.")
# else:
#   print("Sorry you have to grow taller before you can ride.")

# # Multiple If Statements
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster.")
#     age = int(input("How old are you? "))
#     if age <= 12:
#         print("Child tickets are $5.")
#         bill += 5
#     elif age <= 18:
#         print("Youth tickets are $7.")
#         bill += 7
#     else:
#         print("Adult tickets are $12.")
#         bill += 12

#     wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No. ")
#     if wants_photo == "y":
#         bill += 3

#     print(f"Your final bill is {bill}.")
# else:
#     print("Sorry you have to grow taller before you can ride.")
