"""
Warmup

Replace CONDITION with a condition so that the while loop runs until
string has more than 42 charcters in it.
"""

import random

OPTIONS = ["bar", "wubble"]

string = "foo"

while len(string) <= 42:
    string += random.choice(OPTIONS)


print(string)
