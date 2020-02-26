import random

def slug(depth):
    """Simulates Stefanie the slug in the well.
    depth should be positive until Stefanie exits
    the well."""

    day = 0

    while True:
        day += 1

        # Simulate day
        depth -= 3

        print("After day", day, ", Stefanie is at depth", depth)

        # Stop if Stefanie exits well
        if depth <= 0:
            break

        # Simulate night
        depth += random.randint(0, 5)

        print("After night", day, ", Stefanie is at depth", depth)


def main():
    slug(20)

main()
