
def load_grid(filename):
    with open(filename, 'r') as file:
        grid = [[int(val) for val in line.strip()] for line in file]

    return grid
