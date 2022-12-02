
from _utils import load_grid
from _utils import simulate_step
from _utils import print_grid


def are_all_flashing(grid):
    for row in grid:
        for val in row:
            if val != 0:
                return False

    return True


def simulate(grid):

    step = 0
    while True:
        step += 1
        grid, _ = simulate_step(grid)

        if are_all_flashing(grid):
            break

    return grid, step


filename = 'input.dat'
grid = load_grid(filename)

grid, step = simulate(grid)


print(f'What is the first step during which all octopuses flash? {step}')
