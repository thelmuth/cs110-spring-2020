

# divisor = float(input("Enter a number to divide 1 by: "))
# if divisor == 0.0:
#     print("Sorry, can't divide by 0.")
# else:
#     print(1 / divisor)

# Print only the even numbers between 0 and 10:
# for x in range(0, 11, 2):
#     print(x)

# for x in range(11):
#     if x % 2 == 0:
#         print(x)

# Print only the vowels in a person's name
# name = input("Enter your name: ")
# for char in name:
#     if char in "aeiouAEIOU":
#         print(char)

# Print only the vowels in a person's name, all in one string
# name = input("Enter your name: ")
# vowels = ""
# for char in name:
#     if char in "aeiouAEIOU":
#         vowels = vowels + char
# print(vowels)

# How would you change every period in a string into an exclamation point?
# sentence = input("Enter some sentences: ")
# new_sentence = ""
# for char in sentence:
#     if char == ".":
#         new_sentence += "!"
#     else:
#         new_sentence += char
# print(new_sentence)

# Ask for a SSN, and remove all non-numeric characters
# input_ssn = input("Enter your social security number: ")
# ssn = ""
# NUMBERS = "0123456789"
# for char in input_ssn:
#     if char in NUMBERS:
#         ssn += char
#
# print(ssn)


# You can nest for loops:
for ch in "hello":
    print("STARTING INNER LOOP")
    for x in range(5):
        print(ch, x)
    print("ENDING INNER LOOP")









#
