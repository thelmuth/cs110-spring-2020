
# What does this print?

dwight = [["bears", "beets"],
          ["Battlestar", "Galactica"]]

for item in dwight:
    for thing in item:
           print(thing, end="!!!")
    print()
