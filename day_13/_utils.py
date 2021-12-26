
def load_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    grid = []
    for i, line in enumerate(lines):
        if line.strip():
            pos = [int(val) for val in line.strip().split(',')]
            grid.append(pos)
        else:
            break

    instructions = []
    start = len('fold along ')
    for i in range(i + 1, len(lines)):

        line = lines[i].strip()[start:]
        var, value = line.split('=')

        instructions.append((var, int(value)))

    return grid, instructions


def fold_grid(grid, instruction):
    var, value = instruction
    index = 1 if var == 'y' else 0
    for grid_value in grid.copy():
        cmp_value = grid_value[index]
        if cmp_value > value:
            grid_value[index] = 2 * value - cmp_value
            if grid.count(grid_value) > 1:
                grid.remove(grid_value)

    return grid
