

# Assume string_grid is a grid of strings.
# Write a code fragment that counts the number of times the
# string "cat" appears as an element in string_grid and prints that number.

string_grid = [["hi", "cat", "meow"],
               ["cat", "cat", "cat"],
               ["dog", "llama", "cat"]]

count = 0

for row in string_grid:
    for entry in row:
        if entry == "cat":
            count += 1

print(count)
