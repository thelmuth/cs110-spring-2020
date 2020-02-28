
# What does this print?

def main():
    animal = "poodle"
    thing1 = some(some(animal))
    thing2 = some("zebra")
    result = combine(thing2, thing1)
    print(result)

def some(thing1):
    changed = thing1[1:]
    return changed

def combine(thing1, thing2):
    return thing1 + thing2

main()
