
def main():

    # Create a grid of a map for a robot in a park
    map = [["grass", "puddle", "mud"],
           ["tree", "grass", "grass"],
           ["bush", "robot", "tree"],
           ["bush", "mud", "grass"]]

    # print(map)
    # print(map[2])
    # print(map[2][3])

    print_grid(map)

    print(find_element(map, "robot"))
    print(find_element(map, "tree"))
    print(find_element(map, "elephant"))

    print(find_adjacent_same_elements(map))

    num_grid = [[1,2,3,4,5],
                [5,4,1,8,3],
                [4,3,3,2,1],
                [7,7,7,7,7]]

    print(find_element(num_grid, 8))
    print(find_adjacent_same_elements(num_grid))

def print_grid(grid):
    """Nicely prints grid"""
    for row in grid:
        for element in row:
            print("{:6s}".format(element), end=" ")
        print()

def find_element(grid, target):
    """Finds the row and column numbers of target, if it is in the grid."""

    for row_num in range(len(grid)):
        for col_num in range(len(grid[row_num])):
            if grid[row_num][col_num] == target:
                return (row_num, col_num)

    # Returns None if target not found
    return None

def find_adjacent_same_elements(grid):
    """Finds two elements that are adjacent in the same row of the grid.
    Returns (row, col) of the first one."""

    for row_num in range(len(grid)):
        for col_num in range(len(grid[row_num]) - 1):
            if grid[row_num][col_num] == grid[row_num][col_num + 1]:
                return (row_num, col_num)

    return None
















main()
