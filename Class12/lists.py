
# Have user enter 5 names and store in a list

# names = []
# # Using underscore indicates I won't use the loop variable
# for _ in range(5):
#     name = input("Enter a name: ")
#     names.append(name)
#
# print(names)


# Given a list of strings, find and print the longest one.

# strings = ["cat", "Ihave8ch", "donkey", "elephant", "dog", "horse", "12345678"]
#
# longest = ""
# for s in strings:
#     if len(s) > len(longest):
#         longest = s
#
# print(longest)

# Find all of the longest ones in a list

# longest = ""
# longests = []
# for s in strings:
#     if len(s) > len(longest):
#         longest = s
#         longests = [s]
#     elif len(s) == len(longest):
#         longests.append(s)
#
# print(longests)


# Given this list of strings, we want a list of the lengths of those strings
strings = ["cat", "Ihave8ch", "donkey", "elephant", "dog", "horse", "12345678"]

# lengths = []
# for s in strings:
#     lengths.append(len(s))
#
# print(lengths)


# We want to print this list of strings with a separator between each element
separator = "###"

# Easy way:
#print(separator.join(strings))

# What if we were implementing the join method.

result = ""
for s in strings:
    result += s + separator

result = result[:-len(separator)]

print(result)










#
