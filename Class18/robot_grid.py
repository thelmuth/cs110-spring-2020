import random

WIDTH = 12
DIRECTIONS = "UDLR"

def main():

    # BAD: duplicates rows
    # row = ["empty"] * WIDTH
    # room = [row] * WIDTH

    room = []
    for _ in range(WIDTH):
        row = ["dirt"] * WIDTH
        room.append(row)


    # Add robot
    room[3][6] = "robot"


    # add walls
    for col in range(WIDTH):
        room[0][col] = "obstacle"
        room[WIDTH - 1][col] = "obstacle"

    for row in range(WIDTH):
        room[row][0] = "obstacle"
        room[row][WIDTH - 1] = "obstacle"

    print_grid(room)

    # for _ in range(6):
    #     move_robot(room, "D")
    #     print_grid(room)
    #     input()

    clean_room(room)

    print_grid(room)


def print_grid(grid):
    """Nicely prints grid"""
    for row in grid:
        for element in row:
            if element == "robot":
                print("R", end="")
            elif element == "obstacle":
                print("O", end="")
            elif element == "empty":
                print(" ", end="")
            elif element == "dirt":
                print(".", end="")
        print()
    print()

def find_robot(room):
    """Returns the (row, col) of the robot in the room."""

    for row_num in range(len(room)):
        for col_num in range(len(room[0])):
            if room[row_num][col_num] == "robot":
                return (row_num, col_num)


def move_robot(room, direction):
    """Moves robot in this room in specified direction."""

    (robot_row, robot_col) = find_robot(room)

    # Original position of robot
    old_row = robot_row
    old_col = robot_col

    if direction == "L":
        robot_col -= 1
    elif direction == "R":
        robot_col += 1
    elif direction == "U":
        robot_row -= 1
    elif direction == "D":
        robot_row += 1

    if room[robot_row][robot_col] != "obstacle":
        room[robot_row][robot_col] = "robot"
        room[old_row][old_col] = "empty"

def all_clean(room):
    """Returns True if room is clean, False otherwise."""

    for row in room:
        for entry in row:
            if entry == "dirt":
                return False

    return True

def clean_room(room):
    """Randomly moves the robot around the room until it is clean"""

    visits = []
    for _ in range(WIDTH):
        row = [0] * WIDTH
        visits.append(row)

    step = 0
    while not all_clean(room):
        direction = random.choice(DIRECTIONS)
        move_robot(room, direction)

        step += 1
        print("After {} steps, robot moved {}, and the room looks like:".format(step, direction))
        print_grid(room)


        # Record where robot is:
        (robot_row, robot_col) = find_robot(room)
        visits[robot_row][robot_col] += 1

        # input("Press enter to continue:")


    for row in visits:
        print(row)



main()
