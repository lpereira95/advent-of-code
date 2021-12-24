
THRESH = 9


def load_grid(filename):
    with open(filename, 'r') as file:
        grid = [[int(value.strip()) for value in line.strip()] for line in file]

    return grid


def print_grid(grid):
    for row in grid:
        print(''.join([str(val) for val in row]))


def increase_energy_level_all(grid, increment=1):
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            grid[i][j] += increment

    return grid


def get_neighbors(i, j):
    deltas = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1),
              (0, -1), (1, -1))
    neighbors = []
    for delta_i, delta_j in deltas:
        neigh_i = i + delta_i
        neigh_j = j + delta_j
        if neigh_i >= 0 and neigh_j >= 0:
            neighbors.append((neigh_i, neigh_j))

    return neighbors


def flash(grid, i, j):
    total_flashes = 0

    neighbors = get_neighbors(i, j)
    grid[i][j] = 0

    for neighbor in neighbors:
        try:
            neigh_i, neigh_j = neighbor
            if 0 < grid[neigh_i][neigh_j] < THRESH + 1:
                grid[neigh_i][neigh_j] += 1

            if grid[neigh_i][neigh_j] == THRESH + 1:
                grid, total_flashes_ = flash(grid, neigh_i, neigh_j)
                total_flashes += total_flashes_

        except IndexError:
            pass

    return grid, total_flashes + 1


def simulate_step(grid):
    total_flashes = 0
    grid = increase_energy_level_all(grid)

    # flash
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == THRESH + 1:
                grid, total_flashes_ = flash(grid, i, j)
                total_flashes += total_flashes_

    return grid, total_flashes
