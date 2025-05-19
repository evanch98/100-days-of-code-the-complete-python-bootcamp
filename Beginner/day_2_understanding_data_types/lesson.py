# # Primitive Data Types
# # String
# # Subscripting
# print("Hello"[0])
# # Concatenation
# print("123" + "345")

# # Integer = Whole number
# print(123 + 435)

# # Large Integers
# print(123_456_789)

# # Float = Floating Point Number
# print(3.14159)

# # Boolean
# print(True)
# print(False)

# # Type Error, Type Checking, and Type Conversion
# # len(123)  # Error
# print(type(123))
# print(type("abc"))
# print(type(3.14))
# print(type(True))
# print(int("123"))
# print(str(123))
# print(float(123))
# print(bool("123"))
# print("Number of letters in your name: " + str(len(input("Enter your name\n"))))

# # Mathematical Operations
# print(123 + 456)
# print(7 - 3)
# print(3 * 2)
# print(6 / 2)
# print(7 // 2)
# print(6 ** 2)
# print(3 * (3 + 3) / 3 - 3)

# Number manipulation and F Strings
bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))

print(round(bmi))

print(round(bmi, 2))

# f-strings
print(f"Your BMI is {bmi}.")
