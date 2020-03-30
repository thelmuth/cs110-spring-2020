WIDTH = 12

def main():

    # BAD: duplicates rows
    # row = ["empty"] * WIDTH
    # room = [row] * WIDTH

    room = []
    for _ in range(WIDTH):
        row = ["empty"] * WIDTH
        room.append(row)


    # Add robot
    room[3][6] = "robot"


    # add walls
    for col in range(WIDTH):
        room[0][col] = "obstacle"
        room[WIDTH - 1][col] = "obstacle"

    print_grid(room)

def print_grid(grid):
    """Nicely prints grid"""
    for row in grid:
        for element in row:
            print("{:8s}".format(element), end=" ")
        print()


main()
